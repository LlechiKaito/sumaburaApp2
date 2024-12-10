# 技名, 最後の最後のフレーム番号を入力する
from afterProcessing.annotation import Annotation
from backgroundChange import BackgroundChange
import numpy as np

# テストしてないので，よろしく
waza_list = np.array([['jab_0', 100], ['jab_1', 200]])

annotation = Annotation("./../../output/images/b_0", "./../../output/images/b_0", waza_list)
# annotation.annotation_main()
annotation.get_annotation_area("01000.jpg", 0)

backgroundChange = BackgroundChange("./../../input/stage_image", "./../../output/images")
backgroundChange.stage_display()
backgroundChange.stage_resize()
backgroundChange.background_change()