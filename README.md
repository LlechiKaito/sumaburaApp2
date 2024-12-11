<h1>環境構築</h1>

<h2>gitの環境を作る</h2>
<p>
  以下のコマンドでgitをインストールする．</br>
  sudo apt-get install git</br>
  <a href="https://www.kagoya.jp/howto/it-glossary/develop/github_ssh/">
    このサイトを参考にssh接続をする
  </a></br>
  <a href="https://qiita.com/toffy/items/672cd9e2c62a5d897b72">
    port22が拒否されているのならばこのサイトを参考にする
  </a>
</p>

<h2>pythonをインストールする．</h2>
<a href="https://www.python.org/downloads/">
  このサイトを参考にインストールする．
</a>

<h2>pythonの仮想環境を作る．</h2>
<p>
  以下のコマンドで仮想環境を作る．</br>
  python -m venv package または python3 -m venv package
</p>

<h2>仮想環境を有効化する．</h2>
<p>
  以下のコマンドで仮想環境を有効化する．</br>
  source package/bin/activate または ./package/Scripts/activate</br>
  そうしたら(package)と表示される．
</p>

<h2>ライブラリをインストールする．</h2>
<p>
  以下のコマンドでライブラリをインストールする．</br>
  cd src/segment-anything-2</br>
  pip install -e .</br>
  cd checkpoints</br>
  sh download_ckpts.sh</br>
  上記が実行できないならこれで解決するかも→dos2unix download_ckpts.sh</br>
  cd ../../pytorch-yolov3</br>
  pip install -r requirements.txt</br>
  cd ..</br>
  pip install pandas</br>
  pip install natsort</br>
  sudo apt-get install python3-tk</br>
</p>
