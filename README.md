# Optimization
* 最適化全般のプログラム

## リポジトリ構成
```
.
├── README.md                 READMEファイル
├── Dockerfile                Dockerファイル
├── constraints               制約条件ファイル
└── notebook                  jupyter notebook
```

## 環境構築
Dockderfileがあるホスト側のフォルダへ移動（例：Desktop/Optimization）
```
cd Desktop/Optimization
```
Dockerによる環境構築
```
docker build .
```
docker run実行（対象フォルダをマウントする／例：Desktop/Optimization）
```
docker run -p 8888:8888 -v ~/Desktop/Optimization/:/work --name Optimization <docker image>
```
ブラウザーを立ち上げてlocalhost:8888へアクセス
workフォルダ内が対象フォルダにマウントされている

## jupyter notebook説明
* Multi-product_transportation_problem.ipynb : 多品種輸送問題（最適化）のnotebook

## 動作環境
マシンスペック（Mac)
- MacBook Air (Retina, 13-inch, 2018)
- 1.6 GHz デュアルコアIntel Core i5
- 8 GB 2133 MHz LPDDR3