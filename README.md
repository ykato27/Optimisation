# Optimization
* 最適化全般のプログラム

## リポジトリ構成
```
.
├── README.md                 READMEファイル
├── .dockerignore        
├── Dockerfile                Dockerファイル
├── docker-compose.yml
├── constraints               制約条件ファイル
└── notebook                  jupyter notebook
```

## 環境構築

* Dockderfileがあるホスト側のフォルダへ移動（例：Desktop/Optimization）
```
cd Desktop/Optimization
```

* Dockerによる環境構築（フォルダをマウント：Desktop/Optimization）
```
docker-compose up --build
```

* ブラウザーを立ち上げてlocalhost:8888へアクセス
* ローカルフォルダがマウントされている

## jupyter notebook説明
* Multi-product_transportation_problem.ipynb : 多品種輸送問題（最適化）のnotebook

## 動作環境
マシンスペック（Mac)
- MacBook Air (Retina, 13-inch, 2018)
- 1.6 GHz デュアルコアIntel Core i5
- 8 GB 2133 MHz LPDDR3