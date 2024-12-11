# 技名, 最後の最後のフレーム番号を入力する
from annotation import Annotation
from backgroundChange import BackgroundChange
import numpy as np

# # テストしてないので，よろしく
# waza_list = np.array([['jab_0', 100], ['jab_1', 200]])

# annotation = Annotation("./../../output/images/b_0", "./../../output/images/b_0", waza_list)
# # annotation.annotation_main()
# annotation.get_annotation_area("01000.jpg", 0)

backgroundChange = BackgroundChange("../../output/images/jabDa_0", "../../input/images/stage/resize", "../../output/images/senjou/jabDa_0")
# backgroundChange.stage_display()
# backgroundChange.stage_resize()
# backgroundChange.background_change()

backgroundChange.remove_small_objects()

# テストしてないので，よろしく
waza_list = np.array([['jab_0', 100], ['jab_1', 200]])

annotation = Annotation("../../output/images/senjou/jabDa_0", "../../output/images/senjou/jabDa_0", waza_list)
# # annotation.annotation_main()
annotation.get_annotation_area("1274.jpeg", 0)