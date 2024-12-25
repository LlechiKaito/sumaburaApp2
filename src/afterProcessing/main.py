# 技名, 最後の最後のフレーム番号を入力する
from annotation import Annotation
from backgroundChange import BackgroundChange
import numpy as np

# テストしてないので，よろしく
waza_list = np.array([['jab_0', 100], ['jab_1', 200], ['jab_2', 1458]])

annotation = Annotation("../../output/images/jabDa_0/mask_image", "../../output/texts/jabDa_0/", waza_list)
# annotation.remove_small_objects()
annotation.annotation_main()

# backgroundChange = BackgroundChange("../../output/images/jabDa_0/mask_image", "../../input/images/stage/resize", "../../output/images/jabDa_0/senjou")

# backgroundChange.run()