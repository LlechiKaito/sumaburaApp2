# 技名, 最後の最後のフレーム番号を入力する
from annotation import Annotation
from backgroundChange import BackgroundChange
import numpy as np
from resize import Resize

# リサイズ
resize = Resize("../../input/images/B-air_0/resize", "../../input/images/B-air_0/resize2")
resize.resize()
resize = Resize("../../output/images/B-air_0/only_mask", "../../output/images/B-air_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 215], ['B-air', 254], ['notwaza', 416], 
                      ['B-air', 456], ['notwaza', 588], ['B-air', 626], 
                      ['notwaza', 760], ['B-air', 798], ['notwaza', 944], 
                      ['B-air', 982], ['notwaza', 1115], ['B-air', 1154],
                      ['notwaza', 1314], ['B-air', 1352], ['notwaza', 1500],
                      ['B-air', 1542], ['notwaza', 1688], ['B-air', 1730],
                      ['notwaza', 1862], ['B-air', 1898], ['notwaza', 2044],
                      ['B-air', 2082], ['notwaza', 2212], ['B-air', 2250],
                      ['notwaza', 2384], ['B-air', 2422], ['notwaza', 2406],
                      ['B-air', 2444], ['notwaza', 2578], ['B-air', 2616],
                      ['notwaza', 2750], ['B-air', 2790], ['notwaza', 2930],
                      ['B-air', 2966], ['notwaza', 3132], ['B-air', 3154],
                      ['notwaza', 3290], ['B-air', 3328], ['notwaza', 3468],
                      ['B-air', 3508], ['notwaza', 3648], ['B-air', 3688],
                      ['notwaza', 3892]
                    ])

annotation = Annotation("../../output/images/B-air_0/only_mask_resize", "../../output/texts/B-air_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/B-throw_0/resize", "../../input/images/B-throw_0/resize2")
resize.resize()
resize = Resize("../../output/images/B-throw_0/only_mask", "../../output/images/B-throw_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 206], ['Grab', 221], ['B-throw', 251], 
                      ['notwaza', 425], ['Grab', 439], ['B-throw', 469], 
                      ['notwaza', 613], ['Grab', 627], ['B-throw', 657], 
                      ['notwaza', 829], ['Grab', 860], ['B-throw', 873],
                      ['notwaza', 1037], ['Grab', 1065], ['B-throw', 1095],
                      ['notwaza', 1279], ['Grab', 1287], ['B-throw', 1327],
                      ['notwaza', 1501], ['Grab', 1520], ['B-throw', 1551],
                      ['notwaza', 1719], ['Grab', 1737], ['B-throw', 1767],
                      ['notwaza', 2037], ['Grab', 2053], ['B-throw', 2083],
                      ['notwaza', 2275], ['Grab', 2293], ['B-throw', 2323],
                      ['notwaza', 2635], ['Grab', 2655], ['B-throw', 2685],
                      ['notwaza', 2881], ['Grab', 2899], ['B-throw', 2929],
                      ['notwaza', 3123], ['Grab', 3137], ['B-throw', 3167],
                      ['notwaza', 3369], ['Grab', 3408], ['B-throw', 3439],
                      ['notwaza', 3643], ['Grab', 3675], ['B-throw', 3705],
                      ['notwaza', 3904]
                    ])

annotation = Annotation("../../output/images/B-throw_0/only_mask_resize", "../../output/texts/B-throw_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/D-air_0/resize", "../../input/images/D-air_0/resize2")
resize.resize()
resize = Resize("../../output/images/D-air_0/only_mask", "../../output/images/D-air_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 225], ['D-air', 265], ['notwaza', 449], 
                      ['D-air', 489], ['notwaza', 659], ['D-air', 701],
                      ['notwaza', 793], ['D-air', 845], ['notwaza', 965],
                      ['D-air', 1005], ['notwaza', 1141], ['D-air', 1181],
                      ['notwaza', 1297], ['D-air', 1337], ['notwaza', 1469],
                      ['D-air', 1509], ['notwaza', 1649], ['D-air', 1689],
                      ['notwaza', 1815], ['D-air', 1855], ['notwaza', 1994],
                      ['D-air', 2045], ['notwaza', 2151], ['D-air', 2193],
                      ['notwaza', 2365], ['D-air', 2407], ['notwaza', 2543],
                      ['D-air', 2583], ['notwaza', 2741], ['D-air', 2789],
                      ['notwaza', 2927], ['D-air', 2977], ['notwaza', 3067],
                      ['D-air', 3107], ['notwaza', 3245], ['D-air', 3285],
                      ['notwaza', 3405], ['D-air', 3447], ['notwaza', 3607],
                      ['D-air', 3647], ['notwaza', 3814]
                    ])

annotation = Annotation("../../output/images/D-air_0/only_mask_resize", "../../output/texts/D-air_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# # リサイズ
# resize = Resize("../../input/images/D-smash_0/resize", "../../input/images/D-smash_0/resize2")
# resize.resize()
# resize = Resize("../../output/images/D-smash_0/only_mask", "../../output/images/D-smash_0/only_mask_resize")
# resize.resize()

# # 消えているので，別で対応
# waza_list = np.array([['notwaza', 212], ['D-smash', 260], ['notwaza', 396], 
#                       ['D-smash', 444], ['notwaza', 588], ['D-smash', 638],
#                       ['notwaza', 770], ['D-smash', 818], ['notwaza', 938],
#                       ['D-smash', 988], ['notwaza', 1130], ['D-smash', 1178],
#                       ['notwaza', 1426], ['D-smash', 1472], ['notwaza', 1518],
#                       ['D-smash', 1566], ['notwaza', 1702], ['D-smash', 1752],
#                       ['notwaza', 1856], ['D-smash', 1904], ['notwaza', 2036],
#                       ['D-smash', 2084], ['notwaza', 2256], ['D-smash', 2302],
#                       ['notwaza', 2402], ['D-smash', 2448], ['notwaza', 2574],
#                       ['D-smash', 2622], ['notwaza', 2768], ['D-smash', 2816],
#                       ['notwaza', 2940], ['D-smash', 2988], ['notwaza', 3134],
#                       ['D-smash', 3180], ['notwaza', 3278], ['D-smash', 3326],
#                       ['notwaza', 3458], ['D-smash', 3506], ['notwaza', 3644],
#                       ['D-smash', 3692], ['notwaza', 3831]
#                     ])

# annotation = Annotation("../../output/images/D-smash_0/only_mask_resize", "../../output/texts/D-smash_0/", waza_list)
# annotation.remove_small_objects()
# annotation.annotation_main(np.array([401, 402, 403, 404, 405, 406, 407, 408, 593, 594, 595, 596, 597, 598]))

# リサイズ
resize = Resize("../../input/images/D-throw_0/resize", "../../input/images/D-throw_0/resize2")
resize.resize()
resize = Resize("../../output/images/D-throw_0/only_mask", "../../output/images/D-throw_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 195], ['Grab', 209], ['D-throw', 247], 
                      ['notwaza', 411], ['Grab', 426], ['D-throw', 461], 
                      ['notwaza', 613], ['Grab', 631], ['D-throw', 669], 
                      ['notwaza', 825], ['Grab', 845], ['D-throw', 883],
                      ['notwaza', 1085], ['Grab', 1101], ['D-throw', 1139],
                      ['notwaza', 1319], ['Grab', 1337], ['D-throw', 1373],
                      ['notwaza', 1659], ['Grab', 1675], ['D-throw', 1711],
                      ['notwaza', 1875], ['Grab', 1889], ['D-throw', 1927],
                      ['notwaza', 2089], ['Grab', 2103], ['D-throw', 2141],
                      ['notwaza', 2405], ['Grab', 2423], ['D-throw', 2461],
                      ['notwaza', 2643], ['Grab', 2677], ['D-throw', 2713],
                      ['notwaza', 2881], ['Grab', 2895], ['D-throw', 2933],
                      ['notwaza', 3091], ['Grab', 3105], ['D-throw', 3143],
                      ['notwaza', 3301], ['Grab', 3319], ['D-throw', 3357],
                      ['notwaza', 3515], ['Grab', 3529], ['D-throw', 3567],
                      ['notwaza', 3725], ['Grab', 3741], ['D-throw', 3777],
                      ['notwaza', 4010]
                    ])

annotation = Annotation("../../output/images/D-throw_0/only_mask_resize", "../../output/texts/D-throw_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/D-tilt_0/resize", "../../input/images/D-tilt_0/resize2")
resize.resize()
resize = Resize("../../output/images/D-tilt_0/only_mask", "../../output/images/D-tilt_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 200], ['D-tilt', 238], ['notwaza', 380], 
                      ['D-tilt', 416], ['notwaza', 564], ['D-tilt', 600],
                      ['notwaza', 754], ['D-tilt', 792], ['notwaza', 930],
                      ['D-tilt', 966], ['notwaza', 1104], ['D-tilt', 1142],
                      ['notwaza', 1292], ['D-tilt', 1328], ['notwaza', 1474],
                      ['D-tilt', 1510], ['notwaza', 1664], ['D-tilt', 1700],
                      ['notwaza', 1836], ['D-tilt', 1874], ['notwaza', 2044],
                      ['D-tilt', 2080], ['notwaza', 2206], ['D-tilt', 2242],
                      ['notwaza', 2382], ['D-tilt', 2420], ['notwaza', 2562],
                      ['D-tilt', 2600], ['notwaza', 2720], ['D-tilt', 2756],
                      ['notwaza', 2906], ['D-tilt', 2942], ['notwaza', 3080],
                      ['D-tilt', 3116], ['notwaza', 3272], ['D-tilt', 3310],
                      ['notwaza', 3456], ['D-tilt', 3492], ['notwaza', 3638],
                      ['D-tilt', 3674], ['notwaza', 3817]
                    ])

annotation = Annotation("../../output/images/D-tilt_0/only_mask_resize", "../../output/texts/D-tilt_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/DA_0/resize", "../../input/images/DA_0/resize2")
resize.resize()
resize = Resize("../../output/images/DA_0/only_mask", "../../output/images/DA_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 223], ['DA', 265], ['notwaza', 417], 
                      ['DA', 459], ['notwaza', 597], ['DA', 639],
                      ['notwaza', 777], ['DA', 819], ['notwaza', 961],
                      ['DA', 1003], ['notwaza', 1143], ['DA', 1185],
                      ['notwaza', 1335], ['DA', 1377], ['notwaza', 1525],
                      ['DA', 1567], ['notwaza', 1687], ['DA', 1729],
                      ['notwaza', 1869], ['DA', 1911], ['notwaza', 2051],
                      ['DA', 2093], ['notwaza', 2231], ['DA', 2273],
                      ['notwaza', 2419], ['DA', 2461], ['notwaza', 2593],
                      ['DA', 2635], ['notwaza', 2787], ['DA', 2829],
                      ['notwaza', 2973], ['DA', 3015], ['notwaza', 3119],
                      ['DA', 3161], ['notwaza', 3303], ['DA', 3345],
                      ['notwaza', 3541], ['DA', 3583], ['notwaza', 3669],
                      ['DA', 3711], ['notwaza', 3887]
                    ])

annotation = Annotation("../../output/images/DA_0/only_mask_resize", "../../output/texts/DA_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/Down-B_0/resize", "../../input/images/Down-B_0/resize2")
resize.resize()
resize = Resize("../../output/images/Down-B_0/only_mask", "../../output/images/Down-B_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 222], ['Down-B', 294], ['notwaza', 412], 
                      ['Down-B', 484], ['notwaza', 582], ['Down-B', 656],
                      ['notwaza', 778], ['Down-B', 832], ['notwaza', 980],
                      ['Down-B', 1038], ['notwaza', 1160], ['Down-B', 1218],
                      ['notwaza', 1314], ['Down-B', 1370], ['notwaza', 1492],
                      ['Down-B', 1550], ['notwaza', 1642], ['Down-B', 1714],
                      ['notwaza', 1856], ['Down-B', 1928], ['notwaza', 2050],
                      ['Down-B', 2122], ['notwaza', 2230], ['Down-B', 2302],
                      ['notwaza', 2406], ['Down-B', 2478], ['notwaza', 2576],
                      ['Down-B', 2634], ['notwaza', 2770], ['Down-B', 2828],
                      ['notwaza', 2978], ['Down-B', 3034], ['notwaza', 3124],
                      ['Down-B', 3180], ['notwaza', 3296], ['Down-B', 3354],
                      ['notwaza', 3490], ['Down-B', 3514], ['notwaza', 3648],
                      ['Down-B', 3706], ['notwaza', 3899]
                    ])

annotation = Annotation("../../output/images/Down-B_0/only_mask_resize", "../../output/texts/Down-B_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/F-air_0/resize", "../../input/images/F-air_0/resize2")
resize.resize()
resize = Resize("../../output/images/F-air_0/only_mask", "../../output/images/F-air_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 215], ['F-air', 265], ['notwaza', 433], 
                      ['F-air', 483], ['notwaza', 593], ['F-air', 651],
                      ['notwaza', 763], ['F-air', 823], ['notwaza', 945],
                      ['F-air', 995], ['notwaza', 1115], ['F-air', 1165],
                      ['notwaza', 1261], ['F-air', 1311], ['notwaza', 1465],
                      ['F-air', 1507], ['notwaza', 1687], ['F-air', 1733],
                      ['notwaza', 1837], ['F-air', 1897], ['notwaza', 2031],
                      ['F-air', 2091], ['notwaza', 2207], ['F-air', 2257],
                      ['notwaza', 2347], ['F-air', 2403], ['notwaza', 2547],
                      ['F-air', 2581], ['notwaza', 2751], ['F-air', 2801],
                      ['notwaza', 2919], ['F-air', 2963], ['notwaza', 3061],
                      ['F-air', 3111], ['notwaza', 3279], ['F-air', 3339],
                      ['notwaza', 3443], ['F-air', 3503], ['notwaza', 3621],
                      ['F-air', 3681], ['notwaza', 3744]
                    ])

annotation = Annotation("../../output/images/F-air_0/only_mask_resize", "../../output/texts/F-air_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/F-smash_0/resize", "../../input/images/F-smash_0/resize2")
resize.resize()
resize = Resize("../../output/images/F-smash_0/only_mask", "../../output/images/F-smash_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 221], ['F-smash', 277], ['notwaza', 403], 
                      ['F-smash', 460], ['notwaza', 592], ['F-smash', 647],
                      ['notwaza', 778], ['F-smash', 836], ['notwaza', 962],
                      ['F-smash', 1033], ['notwaza', 1124], ['F-smash', 1252],
                      ['notwaza', 1337], ['F-smash', 1411], ['notwaza', 1516],
                      ['F-smash', 1571], ['notwaza', 1637], ['F-smash', 1693],
                      ['notwaza', 1841], ['F-smash', 1974], ['notwaza', 2150],
                      ['F-smash', 2206], ['notwaza', 2304], ['F-smash', 2360],
                      ['notwaza', 2446], ['F-smash', 2506], ['notwaza', 2608],
                      ['F-smash', 2665], ['notwaza', 2755], ['F-smash', 2814],
                      ['notwaza', 2928], ['F-smash', 2984], ['notwaza', 3116],
                      ['F-smash', 3174], ['notwaza', 3300], ['F-smash', 3356],
                      ['notwaza', 3480], ['F-smash', 3536], ['notwaza', 3634],
                      ['F-smash', 3698], ['notwaza', 3814]
                    ])

annotation = Annotation("../../output/images/F-smash_0/only_mask_resize", "../../output/texts/F-smash_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main(np.array([2609, 2610, 2611, 2612, 2613, 2614, 2615, 2616, 2617, 2618, 2619, 2620]))

# リサイズ
resize = Resize("../../input/images/F-throw_0/resize", "../../input/images/F-throw_0/resize2")
resize.resize()
resize = Resize("../../output/images/F-throw_0/only_mask", "../../output/images/F-throw_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 230], ['Grab', 246], ['F-throw', 270], 
                      ['notwaza', 426], ['Grab', 440], ['F-throw', 464], 
                      ['notwaza', 596], ['Grab', 610], ['F-throw', 636], 
                      ['notwaza', 802], ['Grab', 836], ['F-throw', 860],
                      ['notwaza', 1016], ['Grab', 1036], ['F-throw', 1062],
                      ['notwaza', 1232], ['Grab', 1246], ['F-throw', 1270],
                      ['notwaza', 1546], ['Grab', 1564], ['F-throw', 1588],
                      ['notwaza', 1774], ['Grab', 1788], ['F-throw', 1812],
                      ['notwaza', 2042], ['Grab', 2056], ['F-throw', 2080],
                      ['notwaza', 2250], ['Grab', 2266], ['F-throw', 2290],
                      ['notwaza', 2470], ['Grab', 2486], ['F-throw', 2512],
                      ['notwaza', 2710], ['Grab', 2724], ['F-throw', 2748],
                      ['notwaza', 2960], ['Grab', 2974], ['F-throw', 3000],
                      ['notwaza', 3194], ['Grab', 3208], ['F-throw', 3234],
                      ['notwaza', 3446], ['Grab', 3460], ['F-throw', 3486],
                      ['notwaza', 3728], ['Grab', 3742], ['F-throw', 3786],
                      ['notwaza', 3992]
                    ])

annotation = Annotation("../../output/images/F-throw_0/only_mask_resize", "../../output/texts/F-throw_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/F-tilt_0/resize", "../../input/images/F-tilt_0/resize2")
resize.resize()
resize = Resize("../../output/images/F-tilt_0/only_mask", "../../output/images/F-tilt_0/only_mask_resize")
resize.resize()


# テストしてないので，よろしく
waza_list = np.array([['notwaza', 208], ['F-tilt', 250], ['notwaza', 392], 
                      ['F-tilt', 434], ['notwaza', 546], ['F-tilt', 589],
                      ['notwaza', 694], ['F-tilt', 738], ['notwaza', 838],
                      ['F-tilt', 883], ['notwaza', 968], ['F-tilt', 1012],
                      ['notwaza', 1105], ['F-tilt', 1148], ['notwaza', 1226],
                      ['F-tilt', 1268], ['notwaza', 1320], ['F-tilt', 1364],
                      ['notwaza', 1474], ['F-tilt', 1519], ['notwaza', 1598],
                      ['F-tilt', 1642], ['notwaza', 1822], ['F-tilt', 1864],
                      ['notwaza', 2026], ['F-tilt', 2070], ['notwaza', 2206],
                      ['F-tilt', 2248], ['notwaza', 2385], ['F-tilt', 2426],
                      ['notwaza', 2548], ['F-tilt', 2592], ['notwaza', 2739],
                      ['F-tilt', 2781], ['notwaza', 2871], ['F-tilt', 2913],
                      ['notwaza', 3071], ['F-tilt', 3111], ['notwaza', 3139],
                      ['F-tilt', 3181], ['notwaza', 3405], ['F-tilt', 3449],
                      ['notwaza', 3621], ['F-tilt', 3665], ['notwaza', 3827],
                    ])

annotation = Annotation("../../output/images/F-tilt_0/only_mask_resize", "../../output/texts/F-tilt_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/Grab-blow_0/resize", "../../input/images/Grab-blow_0/resize2")
resize.resize()
resize = Resize("../../output/images/Grab-blow_0/only_mask", "../../output/images/Grab-blow_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 197], ['Grab', 231], ['U-throw', 281], 
                      ['notwaza', 427], ['Grab', 453], ['U-throw', 503], 
                      ['notwaza', 613], ['Grab', 653], ['U-throw', 703], 
                      ['notwaza', 933], ['Grab', 959], ['U-throw', 1009],
                      ['notwaza', 1139], ['Grab', 1153], ['Grab-blow', 1177], ['U-throw', 1227],
                      ['notwaza', 1351], ['Grab', 1377], ['U-throw', 1427],
                      ['notwaza', 1581], ['Grab', 1615], ['U-throw', 1665],
                      ['notwaza', 1831], ['Grab', 1865], ['U-throw', 1915],
                      ['notwaza', 2121], ['Grab', 2151], ['U-throw', 2201],
                      ['notwaza', 2387], ['Grab', 2413], ['U-throw', 2463],
                      ['notwaza', 2625], ['Grab', 2659], ['U-throw', 2709],
                      ['notwaza', 2865], ['Grab', 2901], ['U-throw', 2951],
                      ['notwaza', 3109], ['Grab', 3133], ['U-throw', 3181],
                      ['notwaza', 3341], ['Grab', 3363], ['U-throw', 3411],
                      ['notwaza', 3575], ['Grab', 3589], ['U-throw', 3639],
                      ['notwaza', 3931]
                    ])

annotation = Annotation("../../output/images/Grab-blow_0/only_mask_resize", "../../output/texts/Grab-blow_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/Jab_0/resize", "../../input/images/Jab_0/resize2")
resize.resize()
resize = Resize("../../output/images/Jab_0/only_mask", "../../output/images/Jab_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 192], ['Jab1', 206], ['Jab2', 244], 
                      ['notwaza', 382], ['Jab1', 398], ['Jab2', 436], 
                      ['notwaza', 564], ['Jab1', 580], ['Jab2', 620], 
                      ['notwaza', 744], ['Jab1', 758], ['Jab2', 796],
                      ['notwaza', 930], ['Jab1', 944], ['Jab2', 984],
                      ['notwaza', 1142], ['Jab1', 1154], ['Jab2', 1176],
                      ['notwaza', 1294], ['Jab1', 1308], ['Jab2', 1346],
                      ['notwaza', 1486], ['Jab1', 1498], ['Jab2', 1536],
                      ['notwaza', 1650], ['Jab1', 1666], ['Jab2', 1686], ['Jab1', 1702],
                      ['notwaza', 1844], ['Jab1', 1856], ['Jab2', 1894],
                      ['notwaza', 2024], ['Jab1', 2038], ['Jab2', 2076],
                      ['notwaza', 2214], ['Jab1', 2230], ['Jab2', 2264],
                      ['notwaza', 2370], ['Jab1', 2384], ['Jab2', 3402], ['Jab1', 2418],
                      ['notwaza', 2582], ['Jab1', 2594], ['Jab2', 2634],
                      ['notwaza', 2744], ['Jab1', 2756], ['Jab2', 2778],
                      ['notwaza', 2926], ['Jab1', 2940], ['Jab2', 2980],
                      ['notwaza', 3094], ['Jab1', 3108], ['Jab2', 3148],
                      ['notwaza', 3348], ['Jab1', 3360], ['Jab2', 3400],
                      ['notwaza', 3458], ['Jab1', 3474], ['Jab2', 3514],
                      ['notwaza', 3636], ['Jab1', 3656], ['Jab2', 3696],
                      ['notwaza', 3804]
                    ])

annotation = Annotation("../../output/images/Jab_0/only_mask_resize", "../../output/texts/Jab_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/N-air_0/resize", "../../input/images/N-air_0/resize2")
resize.resize()
resize = Resize("../../output/images/N-air_0/only_mask", "../../output/images/N-air_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 229], ['N-air', 267], ['notwaza', 407], 
                      ['N-air', 445], ['notwaza', 587], ['N-air', 625],
                      ['notwaza', 759], ['N-air', 796], ['notwaza', 957],
                      ['N-air', 995], ['notwaza', 1167], ['N-air', 1205],
                      ['notwaza', 1329], ['N-air', 1367], ['notwaza', 1507],
                      ['N-air', 1545], ['notwaza', 1685], ['N-air', 1723],
                      ['notwaza', 1869], ['N-air', 1907], ['notwaza', 2035],
                      ['N-air', 2073], ['notwaza', 2213], ['N-air', 2267],
                      ['notwaza', 2399], ['N-air', 2437], ['notwaza', 2593],
                      ['N-air', 2631], ['notwaza', 2779], ['N-air', 2817],
                      ['notwaza', 2973], ['N-air', 3011], ['notwaza', 3105],
                      ['N-air', 3143], ['notwaza', 3281], ['N-air', 3319],
                      ['notwaza', 3445], ['N-air', 3483], ['notwaza', 3633],
                      ['N-air', 3685], ['notwaza', 3861]
                    ])  

annotation = Annotation("../../output/images/N-air_0/only_mask_resize", "../../output/texts/N-air_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/NB_0/resize", "../../input/images/NB_0/resize2")
resize.resize()
resize = Resize("../../output/images/NB_0/only_mask", "../../output/images/NB_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 218], ['NB', 256], ['notwaza', 426], 
                      ['NB', 466], ['notwaza', 542], ['NB', 584],
                      ['notwaza', 762], ['NB', 802], ['notwaza', 936],
                      ['NB', 978], ['notwaza', 1128], ['NB', 1168],
                      ['notwaza', 1336], ['NB', 1376], ['notwaza', 1518],
                      ['NB', 1560], ['notwaza', 1683], ['NB', 1720],
                      ['notwaza', 1888], ['NB', 1927], ['notwaza', 2004],
                      ['NB', 2044], ['notwaza', 2212], ['NB', 2254],
                      ['notwaza', 2390], ['NB', 2434], ['notwaza', 2568],
                      ['NB', 2608], ['notwaza', 2762], ['NB', 2803],
                      ['notwaza', 2941], ['NB', 2980], ['notwaza', 3120],
                      ['NB', 3161], ['notwaza', 3285], ['NB', 3324],
                      ['notwaza', 3460], ['NB', 3501], ['notwaza', 3643],
                      ['NB', 3683], ['notwaza', 3861]
                    ])  

annotation = Annotation("../../output/images/NB_0/only_mask_resize", "../../output/texts/NB_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/Side-B_0/resize", "../../input/images/Side-B_0/resize2")
resize.resize()
resize = Resize("../../output/images/Side-B_0/only_mask", "../../output/images/Side-B_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 200], ['Side-B', 288], ['notwaza', 414], 
                      ['Side-B', 506], ['notwaza', 636], ['Side-B', 726],
                      ['notwaza', 770], ['Side-B', 876], ['notwaza', 1062],
                      ['Side-B', 1166], ['notwaza', 1332], ['Side-B', 1438],
                      ['notwaza', 1502], ['Side-B', 1624], ['notwaza', 1694],
                      ['Side-B', 1814], ['notwaza', 1912], ['Side-B', 2010],
                      ['notwaza', 2063], ['Side-B', 2152], ['notwaza', 2222],
                      ['Side-B', 2334], ['notwaza', 2408], ['Side-B', 2516],
                      ['notwaza', 2566], ['Side-B', 2706], ['notwaza', 2782],
                      ['Side-B', 2890], ['notwaza', 2994], ['Side-B', 3112],
                      ['notwaza', 3164], ['Side-B', 3264], ['notwaza', 3292],
                      ['Side-B', 3398], ['notwaza', 3450], ['Side-B', 3566],
                      ['notwaza', 3594], ['Side-B', 3728], ['notwaza', 3872]
                    ])  

annotation = Annotation("../../output/images/Side-B_0/only_mask_resize", "../../output/texts/Side-B_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/U-air_0/resize", "../../input/images/U-air_0/resize2")
resize.resize()
resize = Resize("../../output/images/U-air_0/only_mask", "../../output/images/U-air_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 200], ['U-air', 232], ['notwaza', 382], 
                      ['U-air', 414], ['notwaza', 570], ['U-air', 602],
                      ['notwaza', 702], ['U-air', 734], ['notwaza', 926],
                      ['U-air', 958], ['notwaza', 1108], ['U-air', 1140],
                      ['notwaza', 1294], ['U-air', 1326], ['notwaza', 1498],
                      ['U-air', 1532], ['notwaza', 1654], ['U-air', 1664],
                      ['notwaza', 1810], ['U-air', 1844], ['notwaza', 1992],
                      ['U-air', 2026], ['notwaza', 2214], ['U-air', 2248],
                      ['notwaza', 2404], ['U-air', 2438], ['notwaza', 2538],
                      ['U-air', 2572], ['notwaza', 2754], ['U-air', 2786],
                      ['notwaza', 2930], ['U-air', 2964], ['notwaza', 3128],
                      ['U-air', 3162], ['notwaza', 3288], ['U-air', 3322],
                      ['notwaza', 3472], ['U-air', 3506], ['notwaza', 3604],
                      ['U-air', 3638], ['notwaza', 3820]
                    ])  

annotation = Annotation("../../output/images/U-air_0/only_mask_resize", "../../output/texts/U-air_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/U-smash_0/resize", "../../input/images/U-smash_0/resize2")
resize.resize()
resize = Resize("../../output/images/U-smash_0/only_mask", "../../output/images/U-smash_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['notwaza', 213], ['U-smash', 265], ['notwaza', 385], 
                      ['U-smash', 437], ['notwaza', 573], ['U-smash', 625],
                      ['notwaza', 743], ['U-smash', 795], ['notwaza', 929],
                      ['U-smash', 981], ['notwaza', 1113], ['U-smash', 1165],
                      ['notwaza', 1295], ['U-smash', 1347], ['notwaza', 1473],
                      ['U-smash', 1525], ['notwaza', 1657], ['U-smash', 1703],
                      ['notwaza', 1831], ['U-smash', 1879], ['notwaza', 2021],
                      ['U-smash', 2073], ['notwaza', 2203], ['U-smash', 2249],
                      ['notwaza', 2387], ['U-smash', 2439], ['notwaza', 2563],
                      ['U-smash', 2617], ['notwaza', 2753], ['U-smash', 2805],
                      ['notwaza', 2937], ['U-smash', 2985], ['notwaza', 3111],
                      ['U-smash', 3163], ['notwaza', 3283], ['U-smash', 3335],
                      ['notwaza', 3465], ['U-smash', 3517], ['notwaza', 3629],
                      ['U-smash', 3681], ['notwaza', 3825]
                    ])  

annotation = Annotation("../../output/images/U-smash_0/only_mask_resize", "../../output/texts/U-smash_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/U-throw_0/resize", "../../input/images/U-throw_0/resize2")
resize.resize()
resize = Resize("../../output/images/U-throw_0/only_mask", "../../output/images/U-throw_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく(Grab-blowの中にGrab的な要素があるから調整しないといけんかも)
waza_list = np.array([['notwaza', 233], ['Grab', 267], ['Grab-blow', 349], 
                      ['notwaza', 465], ['Grab', 479], ['Grab-blow', 589], 
                      ['notwaza', 681], ['Grab', 695], ['Grab-blow', 809], 
                      ['notwaza', 837], ['Grab', 875], ['notwaza', 885], ['Grab', 899], ['Grab-blow', 1027],
                      ['notwaza', 1016], ['Grab', 1036], ['Grab-blow', 1062],
                      ['notwaza', 1135], ['Grab', 1151], ['Grab-blow', 1289],
                      ['notwaza', 1419], ['Grab', 1433], ['Grab-blow', 1591],
                      ['notwaza', 1759], ['Grab', 1775], ['Grab-blow', 1967],
                      ['notwaza', 2171], ['Grab', 2187], ['Grab-blow', 2403],
                      ['notwaza', 2553], ['Grab', 2567], ['Grab-blow', 2809],
                      ['notwaza', 2939], ['Grab', 2953], ['Grab-blow', 3217],
                      ['notwaza', 3347], ['Grab', 3363], ['Grab-blow', 3659],
                      ['notwaza', 3940]
                    ])

annotation = Annotation("../../output/images/U-throw_0/only_mask_resize", "../../output/texts/U-throw_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/U-tilt_0/resize", "../../input/images/U-tilt_0/resize2")
resize.resize()
resize = Resize("../../output/images/U-tilt_0/only_mask", "../../output/images/U-tilt_0/only_mask_resize")
resize.resize()

waza_list = np.array([['notwaza', 224], ['U-tilt', 272], ['notwaza', 390], 
                      ['U-tilt', 438], ['notwaza', 590], ['U-tilt', 638],
                      ['notwaza', 774], ['U-tilt', 822], ['notwaza', 956],
                      ['U-tilt', 1004], ['notwaza', 1140], ['U-tilt', 1188],
                      ['notwaza', 1322], ['U-tilt', 1356], ['notwaza', 1498],
                      ['U-tilt', 1546], ['notwaza', 1686], ['U-tilt', 1734],
                      ['notwaza', 1866], ['U-tilt', 1914], ['notwaza', 2034],
                      ['U-tilt', 2082], ['notwaza', 2234], ['U-tilt', 2282],
                      ['notwaza', 2416], ['U-tilt', 2464], ['notwaza', 2586],
                      ['U-tilt', 2634], ['notwaza', 2762], ['U-tilt', 2810],
                      ['notwaza', 2956], ['U-tilt', 2986], ['notwaza', 3112],
                      ['U-tilt', 3160], ['notwaza', 3290], ['U-tilt', 3338],
                      ['notwaza', 3474], ['U-tilt', 3522], ['notwaza', 3664],
                      ['U-tilt', 3712], ['notwaza', 3845]
                    ])  

annotation = Annotation("../../output/images/U-tilt_0/only_mask_resize", "../../output/texts/U-tilt_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/Up-B_0/resize", "../../input/images/Up-B_0/resize2")
resize.resize()
resize = Resize("../../output/images/Up-B_0/only_mask", "../../output/images/Up-B_0/only_mask_resize")
resize.resize()

waza_list = np.array([['notwaza', 223], ['Up-B', 271], ['notwaza', 409], 
                      ['Up-B', 457], ['notwaza', 593], ['Up-B', 640],
                      ['notwaza', 750], ['Up-B', 799], ['notwaza', 933],
                      ['Up-B', 981], ['notwaza', 1135], ['Up-B', 1183],
                      ['notwaza', 1331], ['Up-B', 1379], ['notwaza', 1500],
                      ['Up-B', 1549], ['notwaza', 1691], ['Up-B', 1739],
                      ['notwaza', 1861], ['Up-B', 1909], ['notwaza', 2043],
                      ['Up-B', 2091], ['notwaza', 2227], ['Up-B', 2277],
                      ['notwaza', 2371], ['Up-B', 2415], ['notwaza', 2483],
                      ['Up-B', 2531], ['notwaza', 2595], ['Up-B', 2641],
                      ['notwaza', 2773], ['Up-B', 2821], ['notwaza', 2925],
                      ['Up-B', 2973], ['notwaza', 3113], ['Up-B', 3161],
                      ['notwaza', 3313], ['Up-B', 3361], ['notwaza', 3475],
                      ['Up-B', 3521], ['notwaza', 3615], ['Up-B', 3661],
                      ['notwaza', 3859]
                    ])  

annotation = Annotation("../../output/images/Up-B_0/only_mask_resize", "../../output/texts/Up-B_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# backgroundChange = BackgroundChange("../../output/images/jabDa_0/mask_image", "../../input/images/stage/resize", "../../output/images/jabDa_0/senjou")

# backgroundChange.run()

from combination import Combination

combination = Combination("../../output/images/test", "../../input/images/test", "../../output/images/test/result.jpeg")
combination.combine_images()