# -*- coding: utf-8 -*-
#
# 最適化応用技術勉強会　スラブ充当の最適化演習課題
#


#インポート
import pandas as pd
import networkx as nx


#データの読込み処理（インデックス指定）
orders = pd.read_csv("orders.csv", index_col='id')  # 注文データの読込
slabs = pd.read_csv("slabs.csv", index_col='id')    # スラブデータの読込


#
# 紐付可否判定サブルーチン  ◆◆穴埋め(1)◆◆
#
#注文の材質（order[“grade”]）とスラブの材質（slab[“grade”]）が等しい
#スラブ巾（slab[“slab_width”]）は注文のMINスラブ巾（order[“slab_width_min”]）以上
#スラブ巾（slab[“slab_width”]）は注文のMAXスラブ巾（order[“slab_width_max”]）以下
#スラブの特性値（slab[“quality_rank”]）は注文の要求特性値（order[“quality_rank”]）以上のときTrueを,それ以外の時Falseを返す
def can_apply(order, slab):
    if order["grade"] == slab["grade"] and \
       order["slab_width_min"] <= slab["slab_width"] and \
       order["slab_width_max"] >= slab["slab_width"] and \
       order["quality_rank"] <= slab["quality_rank"]:
        return True
    return False

#
# 紐付量計算サブルーチン  ◆◆穴埋め(2)◆◆
#
#注文とスラブが紐付け可能なとき、注文量（order[“weight”]）とスラブ重量(slab[”weight”])の最小値を、それ以外は0を返す
def applicable_quantity(order, slab):
    if can_apply(order, slab):
        return min(order["weight"], slab["weight"])
    return 0

#
# 貪欲法
#
greedy_aq = dict()    #スラブに対する紐付量を保持する辞書を定義
greedy_match = dict() #スラブに対する紐付注文IDを保持する辞書を定義

# ◆◆穴埋め(3)◆◆
for oid, order in orders.iterrows():     #注文のイテレーション(注文ノードを先頭から見ていく)
    for sid, slab in slabs.iterrows():   #スラブのイテレーション(スラブノードを先頭から見ていく)
        if sid in greedy_aq and greedy_aq[sid] > 0: continue   #greedy_aq内の該当するキーの値が0より大きい（すでに紐付いている）とき、次のスラブIDを見る
        aq = applicable_quantity(order, slab)  #紐付け可能な時、紐付け量aqは紐付量計算サブルーチンの戻り値
        if aq > 0:
            greedy_aq[sid] = aq   #スラブに対する紐付量を保持する辞書に紐付け量を追加
            greedy_match[sid] = oid   #スラブに対する紐付注文IDを保持する辞書をに注文IDを追加
            break
#
# 重み付き二部グラフ最大重みマッチング
#
# networkxを用いた二部グラフの生成　　◆◆穴埋め(4)◆◆
G = nx.Graph()   #空の無向グラフオブジェクトを作る
for oid in orders.index:
    G.add_node(oid, bipartite=0)   #注文IDノードを作る

for sid in slabs.index:
    G.add_node(sid, bipartite=1)   #スラブIDノードを作る
    
for oid, order in orders.iterrows():
    for sid, slab in slabs.iterrows():
        aq = applicable_quantity(order, slab)
        if aq > 0: G.add_edge(oid, sid, weight=aq)  #紐付け量>0ならば、その紐付け量を重みとするエッジを張る

# 重み付き最大マッチングの実行
match = nx.max_weight_matching(G)

opt_aq = dict()    #スラブに対する紐付量を保持する辞書を定義
opt_match = dict() #スラブに対する紐付注文IDを保持する辞書を定義

for sid, slab in slabs.iterrows():
    #opt_match[sid] = oid = match[sid]   #スラブに対する紐付量を保持する辞書に紐付け量を追加
    opt_match = oid = match   #スラブに対する紐付量を保持する辞書に紐付け量を追加
    opt_aq[sid] = G.edge[oid][sid]['weight']   #スラブに対する紐付注文IDを保持する辞書をに注文IDを追加


#
# グラフ描画(第1回講義資料、サンプルスクリプトintroduction.pyを参照)
#
left, right = nx.bipartite.sets(G)
pos = dict()
pos.update( {n: (1, i) for i, n in enumerate(left)} )
pos.update( {n: (2, i) for i, n in enumerate(right)} )
nx.draw(G, pos=pos, with_labels=True)

#
# 結果比較
#
print("[greedy] total applied quantity = %d"%sum(greedy_aq.values()))
print("[optimal] total applied quantity = %d"%sum(opt_aq.values()))

