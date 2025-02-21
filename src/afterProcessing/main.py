# 技名, 最後の最後のフレーム番号を入力する
from annotation import Annotation
from backgroundChange import BackgroundChange
import numpy as np
from resize import Resize
from afterProcessing.conbination import Combination

# リサイズ
resize = Resize("../../input/images/B-air_0/resize", "../../input/images/B-air_0/resize2")
resize.resize()
resize = Resize("../../output/images/B-air_0/only_mask", "../../output/images/B-air_0/only_mask_resize")
resize.resize()

# テストしてないので，よろしく
waza_list = np.array([['Notwaza', 215], ['B-air', 254], ['Notwaza', 416], 
                      ['B-air', 456], ['Notwaza', 588], ['B-air', 626], 
                      ['Notwaza', 760], ['B-air', 798], ['Notwaza', 944], 
                      ['B-air', 982], ['Notwaza', 1115], ['B-air', 1154],
                      ['Notwaza', 1314], ['B-air', 1352], ['Notwaza', 1500],
                      ['B-air', 1542], ['Notwaza', 1688], ['B-air', 1730],
                      ['Notwaza', 1862], ['B-air', 1898], ['Notwaza', 2044],
                      ['B-air', 2082], ['Notwaza', 2212], ['B-air', 2250],
                      ['Notwaza', 2384], ['B-air', 2422], ['Notwaza', 2406],
                      ['B-air', 2444], ['Notwaza', 2578], ['B-air', 2616],
                      ['Notwaza', 2750], ['B-air', 2790], ['Notwaza', 2930],
                      ['B-air', 2966], ['Notwaza', 3132], ['B-air', 3154],
                      ['Notwaza', 3290], ['B-air', 3328], ['Notwaza', 3468],
                      ['B-air', 3508], ['Notwaza', 3648], ['B-air', 3688],
                      ['Notwaza', 3892]
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
waza_list = np.array([['Notwaza', 206], ['Grab', 221], ['B-throw', 251], 
                      ['Notwaza', 425], ['Grab', 439], ['B-throw', 469], 
                      ['Notwaza', 613], ['Grab', 627], ['B-throw', 657], 
                      ['Notwaza', 829], ['Grab', 860], ['B-throw', 873],
                      ['Notwaza', 1037], ['Grab', 1065], ['B-throw', 1095],
                      ['Notwaza', 1279], ['Grab', 1287], ['B-throw', 1327],
                      ['Notwaza', 1501], ['Grab', 1520], ['B-throw', 1551],
                      ['Notwaza', 1719], ['Grab', 1737], ['B-throw', 1767],
                      ['Notwaza', 2037], ['Grab', 2053], ['B-throw', 2083],
                      ['Notwaza', 2275], ['Grab', 2293], ['B-throw', 2323],
                      ['Notwaza', 2635], ['Grab', 2655], ['B-throw', 2685],
                      ['Notwaza', 2881], ['Grab', 2899], ['B-throw', 2929],
                      ['Notwaza', 3123], ['Grab', 3137], ['B-throw', 3167],
                      ['Notwaza', 3369], ['Grab', 3408], ['B-throw', 3439],
                      ['Notwaza', 3643], ['Grab', 3675], ['B-throw', 3705],
                      ['Notwaza', 3904]
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
waza_list = np.array([['Notwaza', 225], ['D-air', 265], ['Notwaza', 449], 
                      ['D-air', 489], ['Notwaza', 659], ['D-air', 701],
                      ['Notwaza', 793], ['D-air', 845], ['Notwaza', 965],
                      ['D-air', 1005], ['Notwaza', 1141], ['D-air', 1181],
                      ['Notwaza', 1297], ['D-air', 1337], ['Notwaza', 1469],
                      ['D-air', 1509], ['Notwaza', 1649], ['D-air', 1689],
                      ['Notwaza', 1815], ['D-air', 1855], ['Notwaza', 1994],
                      ['D-air', 2045], ['Notwaza', 2151], ['D-air', 2193],
                      ['Notwaza', 2365], ['D-air', 2407], ['Notwaza', 2543],
                      ['D-air', 2583], ['Notwaza', 2741], ['D-air', 2789],
                      ['Notwaza', 2927], ['D-air', 2977], ['Notwaza', 3067],
                      ['D-air', 3107], ['Notwaza', 3245], ['D-air', 3285],
                      ['Notwaza', 3405], ['D-air', 3447], ['Notwaza', 3607],
                      ['D-air', 3647], ['Notwaza', 3814]
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
# waza_list = np.array([['Notwaza', 212], ['D-smash', 260], ['Notwaza', 396], 
#                       ['D-smash', 444], ['Notwaza', 588], ['D-smash', 638],
#                       ['Notwaza', 770], ['D-smash', 818], ['Notwaza', 938],
#                       ['D-smash', 988], ['Notwaza', 1130], ['D-smash', 1178],
#                       ['Notwaza', 1426], ['D-smash', 1472], ['Notwaza', 1518],
#                       ['D-smash', 1566], ['Notwaza', 1702], ['D-smash', 1752],
#                       ['Notwaza', 1856], ['D-smash', 1904], ['Notwaza', 2036],
#                       ['D-smash', 2084], ['Notwaza', 2256], ['D-smash', 2302],
#                       ['Notwaza', 2402], ['D-smash', 2448], ['Notwaza', 2574],
#                       ['D-smash', 2622], ['Notwaza', 2768], ['D-smash', 2816],
#                       ['Notwaza', 2940], ['D-smash', 2988], ['Notwaza', 3134],
#                       ['D-smash', 3180], ['Notwaza', 3278], ['D-smash', 3326],
#                       ['Notwaza', 3458], ['D-smash', 3506], ['Notwaza', 3644],
#                       ['D-smash', 3692], ['Notwaza', 3831]
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
waza_list = np.array([['Notwaza', 195], ['Grab', 209], ['D-throw', 247], 
                      ['Notwaza', 411], ['Grab', 426], ['D-throw', 461], 
                      ['Notwaza', 613], ['Grab', 631], ['D-throw', 669], 
                      ['Notwaza', 825], ['Grab', 845], ['D-throw', 883],
                      ['Notwaza', 1085], ['Grab', 1101], ['D-throw', 1139],
                      ['Notwaza', 1319], ['Grab', 1337], ['D-throw', 1373],
                      ['Notwaza', 1659], ['Grab', 1675], ['D-throw', 1711],
                      ['Notwaza', 1875], ['Grab', 1889], ['D-throw', 1927],
                      ['Notwaza', 2089], ['Grab', 2103], ['D-throw', 2141],
                      ['Notwaza', 2405], ['Grab', 2423], ['D-throw', 2461],
                      ['Notwaza', 2643], ['Grab', 2677], ['D-throw', 2713],
                      ['Notwaza', 2881], ['Grab', 2895], ['D-throw', 2933],
                      ['Notwaza', 3091], ['Grab', 3105], ['D-throw', 3143],
                      ['Notwaza', 3301], ['Grab', 3319], ['D-throw', 3357],
                      ['Notwaza', 3515], ['Grab', 3529], ['D-throw', 3567],
                      ['Notwaza', 3725], ['Grab', 3741], ['D-throw', 3777],
                      ['Notwaza', 4010]
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
waza_list = np.array([['Notwaza', 200], ['D-tilt', 238], ['Notwaza', 380], 
                      ['D-tilt', 416], ['Notwaza', 564], ['D-tilt', 600],
                      ['Notwaza', 754], ['D-tilt', 792], ['Notwaza', 930],
                      ['D-tilt', 966], ['Notwaza', 1104], ['D-tilt', 1142],
                      ['Notwaza', 1292], ['D-tilt', 1328], ['Notwaza', 1474],
                      ['D-tilt', 1510], ['Notwaza', 1664], ['D-tilt', 1700],
                      ['Notwaza', 1836], ['D-tilt', 1874], ['Notwaza', 2044],
                      ['D-tilt', 2080], ['Notwaza', 2206], ['D-tilt', 2242],
                      ['Notwaza', 2382], ['D-tilt', 2420], ['Notwaza', 2562],
                      ['D-tilt', 2600], ['Notwaza', 2720], ['D-tilt', 2756],
                      ['Notwaza', 2906], ['D-tilt', 2942], ['Notwaza', 3080],
                      ['D-tilt', 3116], ['Notwaza', 3272], ['D-tilt', 3310],
                      ['Notwaza', 3456], ['D-tilt', 3492], ['Notwaza', 3638],
                      ['D-tilt', 3674], ['Notwaza', 3817]
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
waza_list = np.array([['Notwaza', 223], ['DA', 265], ['Notwaza', 417], 
                      ['DA', 459], ['Notwaza', 597], ['DA', 639],
                      ['Notwaza', 777], ['DA', 819], ['Notwaza', 961],
                      ['DA', 1003], ['Notwaza', 1143], ['DA', 1185],
                      ['Notwaza', 1335], ['DA', 1377], ['Notwaza', 1525],
                      ['DA', 1567], ['Notwaza', 1687], ['DA', 1729],
                      ['Notwaza', 1869], ['DA', 1911], ['Notwaza', 2051],
                      ['DA', 2093], ['Notwaza', 2231], ['DA', 2273],
                      ['Notwaza', 2419], ['DA', 2461], ['Notwaza', 2593],
                      ['DA', 2635], ['Notwaza', 2787], ['DA', 2829],
                      ['Notwaza', 2973], ['DA', 3015], ['Notwaza', 3119],
                      ['DA', 3161], ['Notwaza', 3303], ['DA', 3345],
                      ['Notwaza', 3541], ['DA', 3583], ['Notwaza', 3669],
                      ['DA', 3711], ['Notwaza', 3887]
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
waza_list = np.array([['Notwaza', 222], ['Down-B', 294], ['Notwaza', 412], 
                      ['Down-B', 484], ['Notwaza', 582], ['Down-B', 656],
                      ['Notwaza', 778], ['Down-B', 832], ['Notwaza', 980],
                      ['Down-B', 1038], ['Notwaza', 1160], ['Down-B', 1218],
                      ['Notwaza', 1314], ['Down-B', 1370], ['Notwaza', 1492],
                      ['Down-B', 1550], ['Notwaza', 1642], ['Down-B', 1714],
                      ['Notwaza', 1856], ['Down-B', 1928], ['Notwaza', 2050],
                      ['Down-B', 2122], ['Notwaza', 2230], ['Down-B', 2302],
                      ['Notwaza', 2406], ['Down-B', 2478], ['Notwaza', 2576],
                      ['Down-B', 2634], ['Notwaza', 2770], ['Down-B', 2828],
                      ['Notwaza', 2978], ['Down-B', 3034], ['Notwaza', 3124],
                      ['Down-B', 3180], ['Notwaza', 3296], ['Down-B', 3354],
                      ['Notwaza', 3490], ['Down-B', 3514], ['Notwaza', 3648],
                      ['Down-B', 3706], ['Notwaza', 3899]
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
waza_list = np.array([['Notwaza', 215], ['F-air', 265], ['Notwaza', 433], 
                      ['F-air', 483], ['Notwaza', 593], ['F-air', 651],
                      ['Notwaza', 763], ['F-air', 823], ['Notwaza', 945],
                      ['F-air', 995], ['Notwaza', 1115], ['F-air', 1165],
                      ['Notwaza', 1261], ['F-air', 1311], ['Notwaza', 1465],
                      ['F-air', 1507], ['Notwaza', 1687], ['F-air', 1733],
                      ['Notwaza', 1837], ['F-air', 1897], ['Notwaza', 2031],
                      ['F-air', 2091], ['Notwaza', 2207], ['F-air', 2257],
                      ['Notwaza', 2347], ['F-air', 2403], ['Notwaza', 2547],
                      ['F-air', 2581], ['Notwaza', 2751], ['F-air', 2801],
                      ['Notwaza', 2919], ['F-air', 2963], ['Notwaza', 3061],
                      ['F-air', 3111], ['Notwaza', 3279], ['F-air', 3339],
                      ['Notwaza', 3443], ['F-air', 3503], ['Notwaza', 3621],
                      ['F-air', 3681], ['Notwaza', 3744]
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
waza_list = np.array([['Notwaza', 221], ['F-smash', 277], ['Notwaza', 403], 
                      ['F-smash', 460], ['Notwaza', 592], ['F-smash', 647],
                      ['Notwaza', 778], ['F-smash', 836], ['Notwaza', 962],
                      ['F-smash', 1033], ['Notwaza', 1124], ['F-smash', 1252],
                      ['Notwaza', 1337], ['F-smash', 1411], ['Notwaza', 1516],
                      ['F-smash', 1571], ['Notwaza', 1637], ['F-smash', 1693],
                      ['Notwaza', 1841], ['F-smash', 1974], ['Notwaza', 2150],
                      ['F-smash', 2206], ['Notwaza', 2304], ['F-smash', 2360],
                      ['Notwaza', 2446], ['F-smash', 2506], ['Notwaza', 2608],
                      ['F-smash', 2665], ['Notwaza', 2755], ['F-smash', 2814],
                      ['Notwaza', 2928], ['F-smash', 2984], ['Notwaza', 3116],
                      ['F-smash', 3174], ['Notwaza', 3300], ['F-smash', 3356],
                      ['Notwaza', 3480], ['F-smash', 3536], ['Notwaza', 3634],
                      ['F-smash', 3698], ['Notwaza', 3814]
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
waza_list = np.array([['Notwaza', 230], ['Grab', 246], ['F-throw', 270], 
                      ['Notwaza', 426], ['Grab', 440], ['F-throw', 464], 
                      ['Notwaza', 596], ['Grab', 610], ['F-throw', 636], 
                      ['Notwaza', 802], ['Grab', 836], ['F-throw', 860],
                      ['Notwaza', 1016], ['Grab', 1036], ['F-throw', 1062],
                      ['Notwaza', 1232], ['Grab', 1246], ['F-throw', 1270],
                      ['Notwaza', 1546], ['Grab', 1564], ['F-throw', 1588],
                      ['Notwaza', 1774], ['Grab', 1788], ['F-throw', 1812],
                      ['Notwaza', 2042], ['Grab', 2056], ['F-throw', 2080],
                      ['Notwaza', 2250], ['Grab', 2266], ['F-throw', 2290],
                      ['Notwaza', 2470], ['Grab', 2486], ['F-throw', 2512],
                      ['Notwaza', 2710], ['Grab', 2724], ['F-throw', 2748],
                      ['Notwaza', 2960], ['Grab', 2974], ['F-throw', 3000],
                      ['Notwaza', 3194], ['Grab', 3208], ['F-throw', 3234],
                      ['Notwaza', 3446], ['Grab', 3460], ['F-throw', 3486],
                      ['Notwaza', 3728], ['Grab', 3742], ['F-throw', 3786],
                      ['Notwaza', 3992]
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
waza_list = np.array([['Notwaza', 208], ['F-tilt', 250], ['Notwaza', 392], 
                      ['F-tilt', 434], ['Notwaza', 546], ['F-tilt', 589],
                      ['Notwaza', 694], ['F-tilt', 738], ['Notwaza', 838],
                      ['F-tilt', 883], ['Notwaza', 968], ['F-tilt', 1012],
                      ['Notwaza', 1105], ['F-tilt', 1148], ['Notwaza', 1226],
                      ['F-tilt', 1268], ['Notwaza', 1320], ['F-tilt', 1364],
                      ['Notwaza', 1474], ['F-tilt', 1519], ['Notwaza', 1598],
                      ['F-tilt', 1642], ['Notwaza', 1822], ['F-tilt', 1864],
                      ['Notwaza', 2026], ['F-tilt', 2070], ['Notwaza', 2206],
                      ['F-tilt', 2248], ['Notwaza', 2385], ['F-tilt', 2426],
                      ['Notwaza', 2548], ['F-tilt', 2592], ['Notwaza', 2739],
                      ['F-tilt', 2781], ['Notwaza', 2871], ['F-tilt', 2913],
                      ['Notwaza', 3071], ['F-tilt', 3111], ['Notwaza', 3139],
                      ['F-tilt', 3181], ['Notwaza', 3405], ['F-tilt', 3449],
                      ['Notwaza', 3621], ['F-tilt', 3665], ['Notwaza', 3827],
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
waza_list = np.array([['Notwaza', 197], ['Grab', 231], ['U-throw', 281], 
                      ['Notwaza', 427], ['Grab', 453], ['U-throw', 503], 
                      ['Notwaza', 613], ['Grab', 653], ['U-throw', 703], 
                      ['Notwaza', 933], ['Grab', 959], ['U-throw', 1009],
                      ['Notwaza', 1139], ['Grab', 1153], ['Grab-blow', 1177], ['U-throw', 1227],
                      ['Notwaza', 1351], ['Grab', 1377], ['U-throw', 1427],
                      ['Notwaza', 1581], ['Grab', 1615], ['U-throw', 1665],
                      ['Notwaza', 1831], ['Grab', 1865], ['U-throw', 1915],
                      ['Notwaza', 2121], ['Grab', 2151], ['U-throw', 2201],
                      ['Notwaza', 2387], ['Grab', 2413], ['U-throw', 2463],
                      ['Notwaza', 2625], ['Grab', 2659], ['U-throw', 2709],
                      ['Notwaza', 2865], ['Grab', 2901], ['U-throw', 2951],
                      ['Notwaza', 3109], ['Grab', 3133], ['U-throw', 3181],
                      ['Notwaza', 3341], ['Grab', 3363], ['U-throw', 3411],
                      ['Notwaza', 3575], ['Grab', 3589], ['U-throw', 3639],
                      ['Notwaza', 3931]
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
waza_list = np.array([['Notwaza', 192], ['Jab1', 206], ['Jab2', 244], 
                      ['Notwaza', 382], ['Jab1', 398], ['Jab2', 436], 
                      ['Notwaza', 564], ['Jab1', 580], ['Jab2', 620], 
                      ['Notwaza', 744], ['Jab1', 758], ['Jab2', 796],
                      ['Notwaza', 930], ['Jab1', 944], ['Jab2', 984],
                      ['Notwaza', 1142], ['Jab1', 1154], ['Jab2', 1176],
                      ['Notwaza', 1294], ['Jab1', 1308], ['Jab2', 1346],
                      ['Notwaza', 1486], ['Jab1', 1498], ['Jab2', 1536],
                      ['Notwaza', 1650], ['Jab1', 1666], ['Jab2', 1686], ['Jab1', 1702],
                      ['Notwaza', 1844], ['Jab1', 1856], ['Jab2', 1894],
                      ['Notwaza', 2024], ['Jab1', 2038], ['Jab2', 2076],
                      ['Notwaza', 2214], ['Jab1', 2230], ['Jab2', 2264],
                      ['Notwaza', 2370], ['Jab1', 2384], ['Jab2', 3402], ['Jab1', 2418],
                      ['Notwaza', 2582], ['Jab1', 2594], ['Jab2', 2634],
                      ['Notwaza', 2744], ['Jab1', 2756], ['Jab2', 2778],
                      ['Notwaza', 2926], ['Jab1', 2940], ['Jab2', 2980],
                      ['Notwaza', 3094], ['Jab1', 3108], ['Jab2', 3148],
                      ['Notwaza', 3348], ['Jab1', 3360], ['Jab2', 3400],
                      ['Notwaza', 3458], ['Jab1', 3474], ['Jab2', 3514],
                      ['Notwaza', 3636], ['Jab1', 3656], ['Jab2', 3696],
                      ['Notwaza', 3804]
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
waza_list = np.array([['Notwaza', 229], ['N-air', 267], ['Notwaza', 407], 
                      ['N-air', 445], ['Notwaza', 587], ['N-air', 625],
                      ['Notwaza', 759], ['N-air', 796], ['Notwaza', 957],
                      ['N-air', 995], ['Notwaza', 1167], ['N-air', 1205],
                      ['Notwaza', 1329], ['N-air', 1367], ['Notwaza', 1507],
                      ['N-air', 1545], ['Notwaza', 1685], ['N-air', 1723],
                      ['Notwaza', 1869], ['N-air', 1907], ['Notwaza', 2035],
                      ['N-air', 2073], ['Notwaza', 2213], ['N-air', 2267],
                      ['Notwaza', 2399], ['N-air', 2437], ['Notwaza', 2593],
                      ['N-air', 2631], ['Notwaza', 2779], ['N-air', 2817],
                      ['Notwaza', 2973], ['N-air', 3011], ['Notwaza', 3105],
                      ['N-air', 3143], ['Notwaza', 3281], ['N-air', 3319],
                      ['Notwaza', 3445], ['N-air', 3483], ['Notwaza', 3633],
                      ['N-air', 3685], ['Notwaza', 3861]
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
waza_list = np.array([['Notwaza', 218], ['NB', 256], ['Notwaza', 426], 
                      ['NB', 466], ['Notwaza', 542], ['NB', 584],
                      ['Notwaza', 762], ['NB', 802], ['Notwaza', 936],
                      ['NB', 978], ['Notwaza', 1128], ['NB', 1168],
                      ['Notwaza', 1336], ['NB', 1376], ['Notwaza', 1518],
                      ['NB', 1560], ['Notwaza', 1683], ['NB', 1720],
                      ['Notwaza', 1888], ['NB', 1927], ['Notwaza', 2004],
                      ['NB', 2044], ['Notwaza', 2212], ['NB', 2254],
                      ['Notwaza', 2390], ['NB', 2434], ['Notwaza', 2568],
                      ['NB', 2608], ['Notwaza', 2762], ['NB', 2803],
                      ['Notwaza', 2941], ['NB', 2980], ['Notwaza', 3120],
                      ['NB', 3161], ['Notwaza', 3285], ['NB', 3324],
                      ['Notwaza', 3460], ['NB', 3501], ['Notwaza', 3643],
                      ['NB', 3683], ['Notwaza', 3861]
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
waza_list = np.array([['Notwaza', 200], ['Side-B', 288], ['Notwaza', 414], 
                      ['Side-B', 506], ['Notwaza', 636], ['Side-B', 726],
                      ['Notwaza', 770], ['Side-B', 876], ['Notwaza', 1062],
                      ['Side-B', 1166], ['Notwaza', 1332], ['Side-B', 1438],
                      ['Notwaza', 1502], ['Side-B', 1624], ['Notwaza', 1694],
                      ['Side-B', 1814], ['Notwaza', 1912], ['Side-B', 2010],
                      ['Notwaza', 2063], ['Side-B', 2152], ['Notwaza', 2222],
                      ['Side-B', 2334], ['Notwaza', 2408], ['Side-B', 2516],
                      ['Notwaza', 2566], ['Side-B', 2706], ['Notwaza', 2782],
                      ['Side-B', 2890], ['Notwaza', 2994], ['Side-B', 3112],
                      ['Notwaza', 3164], ['Side-B', 3264], ['Notwaza', 3292],
                      ['Side-B', 3398], ['Notwaza', 3450], ['Side-B', 3566],
                      ['Notwaza', 3594], ['Side-B', 3728], ['Notwaza', 3872]
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
waza_list = np.array([['Notwaza', 200], ['U-air', 232], ['Notwaza', 382], 
                      ['U-air', 414], ['Notwaza', 570], ['U-air', 602],
                      ['Notwaza', 702], ['U-air', 734], ['Notwaza', 926],
                      ['U-air', 958], ['Notwaza', 1108], ['U-air', 1140],
                      ['Notwaza', 1294], ['U-air', 1326], ['Notwaza', 1498],
                      ['U-air', 1532], ['Notwaza', 1654], ['U-air', 1664],
                      ['Notwaza', 1810], ['U-air', 1844], ['Notwaza', 1992],
                      ['U-air', 2026], ['Notwaza', 2214], ['U-air', 2248],
                      ['Notwaza', 2404], ['U-air', 2438], ['Notwaza', 2538],
                      ['U-air', 2572], ['Notwaza', 2754], ['U-air', 2786],
                      ['Notwaza', 2930], ['U-air', 2964], ['Notwaza', 3128],
                      ['U-air', 3162], ['Notwaza', 3288], ['U-air', 3322],
                      ['Notwaza', 3472], ['U-air', 3506], ['Notwaza', 3604],
                      ['U-air', 3638], ['Notwaza', 3820]
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
waza_list = np.array([['Notwaza', 213], ['U-smash', 265], ['Notwaza', 385], 
                      ['U-smash', 437], ['Notwaza', 573], ['U-smash', 625],
                      ['Notwaza', 743], ['U-smash', 795], ['Notwaza', 929],
                      ['U-smash', 981], ['Notwaza', 1113], ['U-smash', 1165],
                      ['Notwaza', 1295], ['U-smash', 1347], ['Notwaza', 1473],
                      ['U-smash', 1525], ['Notwaza', 1657], ['U-smash', 1703],
                      ['Notwaza', 1831], ['U-smash', 1879], ['Notwaza', 2021],
                      ['U-smash', 2073], ['Notwaza', 2203], ['U-smash', 2249],
                      ['Notwaza', 2387], ['U-smash', 2439], ['Notwaza', 2563],
                      ['U-smash', 2617], ['Notwaza', 2753], ['U-smash', 2805],
                      ['Notwaza', 2937], ['U-smash', 2985], ['Notwaza', 3111],
                      ['U-smash', 3163], ['Notwaza', 3283], ['U-smash', 3335],
                      ['Notwaza', 3465], ['U-smash', 3517], ['Notwaza', 3629],
                      ['U-smash', 3681], ['Notwaza', 3825]
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
waza_list = np.array([['Notwaza', 233], ['Grab', 267], ['Grab-blow', 349], 
                      ['Notwaza', 465], ['Grab', 479], ['Grab-blow', 589], 
                      ['Notwaza', 681], ['Grab', 695], ['Grab-blow', 809], 
                      ['Notwaza', 837], ['Grab', 875], ['Notwaza', 885], ['Grab', 899], ['Grab-blow', 1027],
                      ['Notwaza', 1016], ['Grab', 1036], ['Grab-blow', 1062],
                      ['Notwaza', 1135], ['Grab', 1151], ['Grab-blow', 1289],
                      ['Notwaza', 1419], ['Grab', 1433], ['Grab-blow', 1591],
                      ['Notwaza', 1759], ['Grab', 1775], ['Grab-blow', 1967],
                      ['Notwaza', 2171], ['Grab', 2187], ['Grab-blow', 2403],
                      ['Notwaza', 2553], ['Grab', 2567], ['Grab-blow', 2809],
                      ['Notwaza', 2939], ['Grab', 2953], ['Grab-blow', 3217],
                      ['Notwaza', 3347], ['Grab', 3363], ['Grab-blow', 3659],
                      ['Notwaza', 3940]
                    ])

annotation = Annotation("../../output/images/U-throw_0/only_mask_resize", "../../output/texts/U-throw_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/U-tilt_0/resize", "../../input/images/U-tilt_0/resize2")
resize.resize()
resize = Resize("../../output/images/U-tilt_0/only_mask", "../../output/images/U-tilt_0/only_mask_resize")
resize.resize()

waza_list = np.array([['Notwaza', 224], ['U-tilt', 272], ['Notwaza', 390], 
                      ['U-tilt', 438], ['Notwaza', 590], ['U-tilt', 638],
                      ['Notwaza', 774], ['U-tilt', 822], ['Notwaza', 956],
                      ['U-tilt', 1004], ['Notwaza', 1140], ['U-tilt', 1188],
                      ['Notwaza', 1322], ['U-tilt', 1356], ['Notwaza', 1498],
                      ['U-tilt', 1546], ['Notwaza', 1686], ['U-tilt', 1734],
                      ['Notwaza', 1866], ['U-tilt', 1914], ['Notwaza', 2034],
                      ['U-tilt', 2082], ['Notwaza', 2234], ['U-tilt', 2282],
                      ['Notwaza', 2416], ['U-tilt', 2464], ['Notwaza', 2586],
                      ['U-tilt', 2634], ['Notwaza', 2762], ['U-tilt', 2810],
                      ['Notwaza', 2956], ['U-tilt', 2986], ['Notwaza', 3112],
                      ['U-tilt', 3160], ['Notwaza', 3290], ['U-tilt', 3338],
                      ['Notwaza', 3474], ['U-tilt', 3522], ['Notwaza', 3664],
                      ['U-tilt', 3712], ['Notwaza', 3845]
                    ])  

annotation = Annotation("../../output/images/U-tilt_0/only_mask_resize", "../../output/texts/U-tilt_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# リサイズ
resize = Resize("../../input/images/Up-B_0/resize", "../../input/images/Up-B_0/resize2")
resize.resize()
resize = Resize("../../output/images/Up-B_0/only_mask", "../../output/images/Up-B_0/only_mask_resize")
resize.resize()

waza_list = np.array([['Notwaza', 223], ['Up-B', 271], ['Notwaza', 409], 
                      ['Up-B', 457], ['Notwaza', 593], ['Up-B', 640],
                      ['Notwaza', 750], ['Up-B', 799], ['Notwaza', 933],
                      ['Up-B', 981], ['Notwaza', 1135], ['Up-B', 1183],
                      ['Notwaza', 1331], ['Up-B', 1379], ['Notwaza', 1500],
                      ['Up-B', 1549], ['Notwaza', 1691], ['Up-B', 1739],
                      ['Notwaza', 1861], ['Up-B', 1909], ['Notwaza', 2043],
                      ['Up-B', 2091], ['Notwaza', 2227], ['Up-B', 2277],
                      ['Notwaza', 2371], ['Up-B', 2415], ['Notwaza', 2483],
                      ['Up-B', 2531], ['Notwaza', 2595], ['Up-B', 2641],
                      ['Notwaza', 2773], ['Up-B', 2821], ['Notwaza', 2925],
                      ['Up-B', 2973], ['Notwaza', 3113], ['Up-B', 3161],
                      ['Notwaza', 3313], ['Up-B', 3361], ['Notwaza', 3475],
                      ['Up-B', 3521], ['Notwaza', 3615], ['Up-B', 3661],
                      ['Notwaza', 3859]
                    ])  

annotation = Annotation("../../output/images/Up-B_0/only_mask_resize", "../../output/texts/Up-B_0/", waza_list)
annotation.remove_small_objects()
annotation.annotation_main()

# ここからテストデータのアノテーション

# リサイズ
resize = Resize("../../input/images/air_test_0/resize", "../../input/images/air_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 118], ['N-air', 156], ['Notwaza', 186], 
                      ['U-air', 214], ['Notwaza', 262], ['F-air', 299],
                      ['Notwaza', 348], ['B-air', 385], ['Notwaza', 421],
                      ['D-air', 464], ['Notwaza', 546], ['U-air', 576],
                      ['Notwaza', 610], ['F-air', 648], ['Notwaza', 684],
                      ['D-air', 724], ['Notwaza', 762], ['B-air', 800],
                      ['Notwaza', 822], ['N-air', 859], ['Notwaza', 924]
                    ])  

annotation = Annotation("../../input/images/air_test_0/resize2", "../../output/texts/air_test_0/", waza_list)
annotation.annotation_main_test()

# リサイズ
resize = Resize("../../input/images/b_test_0/resize", "../../input/images/b_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 86], ['Up-B', 133], ['Notwaza', 206], 
                      ['Side-B', 290], ['Notwaza', 308], ['Down-B', 386],
                      ['Notwaza', 404], ['N-air', 442], ['Notwaza', 488],
                      ['Up-B', 537], ['Notwaza', 568], ['NB', 610],
                      ['Notwaza', 623], ['Side-B', 735], ['Notwaza', 826],
                      ['Down-B', 903], ['Notwaza', 958]
                    ])  

annotation = Annotation("../../input/images/b_test_0/resize2", "../../output/texts/b_test_0/", waza_list)
annotation.annotation_main_test()

# リサイズ
resize = Resize("../../input/images/jabDa_test_0/resize", "../../input/images/jabDa_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 79], ['DA', 123], ['Notwaza', 147], 
                      ['Jab1', 159], ['Jab2', 193], ['Notwaza', 213],
                      ['DA', 255], ['Notwaza', 267], ['Jab1', 279],
                      ['Jab2', 319], ['Notwaza', 389]
                    ])  

annotation = Annotation("../../input/images/jabDa_test_0/resize2", "../../output/texts/jabDa_test_0/", waza_list)
annotation.annotation_main_test()

# リサイズ
resize = Resize("../../input/images/nb_test_0/resize", "../../input/images/nb_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 112], ['NB', 154], ['Notwaza', 228],
                      ['NB', 268], ['Notwaza', 333]
                    ])  

annotation = Annotation("../../input/images/nb_test_0/resize2", "../../output/texts/nb_test_0/", waza_list)
annotation.annotation_main_test()

# リサイズ
resize = Resize("../../input/images/smash_test_0/resize", "../../input/images/smash_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 93], ['U-smash', 143], ['Notwaza', 161], 
                      ['F-smash', 219], ['Notwaza', 229], ['D-smash', 287],
                      ['Notwaza', 327], ['U-smash', 379], ['Notwaza', 387],
                      ['F-smash', 445], ['Notwaza', 463], ['D-smash', 523],
                      ['Notwaza', 582]
                    ])  

annotation = Annotation("../../input/images/smash_test_0/resize2", "../../output/texts/smash_test_0/", waza_list)
annotation.annotation_main_test()

# リサイズ
resize = Resize("../../input/images/tilt_test_0/resize", "../../input/images/tilt_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 82], ['U-tilt', 130], ['Notwaza', 152], 
                      ['F-tilt', 196], ['Notwaza', 216], ['D-tilt', 258],
                      ['Notwaza', 352], ['U-tilt', 400], ['Notwaza', 420],
                      ['F-tilt', 464], ['Notwaza', 490], ['D-tilt', 532],
                      ['Notwaza', 579]
                    ])  

annotation = Annotation("../../input/images/tilt_test_0/resize2", "../../output/texts/tilt_test_0/", waza_list)
annotation.annotation_main_test()

# リサイズ
resize = Resize("../../input/images/tilt_test_0/resize", "../../input/images/tilt_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 82], ['U-tilt', 130], ['Notwaza', 152], 
                      ['F-tilt', 196], ['Notwaza', 216], ['D-tilt', 258],
                      ['Notwaza', 352], ['U-tilt', 400], ['Notwaza', 420],
                      ['F-tilt', 464], ['Notwaza', 490], ['D-tilt', 532],
                      ['Notwaza', 579]
                    ])

annotation = Annotation("../../input/images/tilt_test_0/resize2", "../../output/texts/tilt_test_0/", waza_list)
annotation.annotation_main_test()

# リサイズ
resize = Resize("../../input/images/grab_test_0/resize", "../../input/images/grab_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 88], ['Grab', 142], ['Grab-blow', 180], 
                      ['Grab', 204], ['Notwaza', 298], ['Grab', 340],
                      ['U-throw', 390], ['Notwaza', 520], ['Grab', 554],
                      ['B-throw', 586], ['Notwaza', 730], ['Grab', 808],
                      ['F-throw', 834], ['Notwaza', 990], ['Grab', 1006],
                      ['D-throw', 1044], ['Notwaza', 1196], ['Grab', 1232],
                      ['Grab-blow', 1274], ['Grab', 1340], ['F-throw', 1366],
                      ['Notwaza', 1526], ['Grab', 1562], ['U-throw', 1592],
                      ['Notwaza', 1756], ['Grab', 1776], ['B-throw', 1806],
                      ['Notwaza', 1966], ['Grab', 1984], ['D-throw', 2022],
                      ['Notwaza', 2117]
                    ])

annotation = Annotation("../../input/images/grab_test_0/resize2", "../../output/texts/grab_test_0/", waza_list)
annotation.annotation_main_test()

# 戦場のテストデータの作成

# リサイズ
resize = Resize("../../input/images/air_senjou_test_0/resize", "../../input/images/air_senjou_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 122], ['N-air', 158], ['Notwaza', 207], 
                      ['U-air', 239], ['Notwaza', 275], ['B-air', 313],
                      ['Notwaza', 363], ['F-air', 406], ['Notwaza', 447],
                      ['D-air', 487], ['Notwaza', 597], ['U-air', 627],
                      ['Notwaza', 665], ['N-air', 703], ['Notwaza', 751],
                      ['F-air', 789], ['Notwaza', 835], ['B-air', 875],
                      ['Notwaza', 909], ['D-air', 949], ['Notwaza', 1033]
                    ])

annotation = Annotation("../../input/images/air_senjou_test_0/resize2", "../../output/texts/air_senjou_test_0/", waza_list)
annotation.annotation_main_test()

# リサイズ
resize = Resize("../../input/images/b_senjou_test_0/resize", "../../input/images/b_senjou_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 103], ['NB', 147], ['Notwaza', 167], 
                      ['Up-B', 215], ['Notwaza', 241], ['Down-B', 314],
                      ['Notwaza', 345], ['Side-B', 445], ['Notwaza', 499],
                      ['NB', 539], ['Notwaza', 561], ['NB', 602],
                      ['Notwaza', 613], ['Up-B', 661], ['Notwaza', 677],
                      ['Down-B', 751], ['Notwaza', 761], ['Side-B', 873],
                      ['Notwaza', 930]
                    ])

annotation = Annotation("../../input/images/b_senjou_test_0/resize2", "../../output/texts/b_senjou_test_0/", waza_list)
annotation.annotation_main_test()

# リサイズ
resize = Resize("../../input/images/smash_senjou_test_0/resize", "../../input/images/smash_senjou_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 125], ['U-smash', 175], ['Notwaza', 201], 
                      ['F-smash', 259], ['Notwaza', 281], ['D-smash', 339],
                      ['Notwaza', 391], ['U-smash', 441], ['Notwaza', 449],
                      ['F-smash', 507], ['Notwaza', 515], ['D-smash', 578],
                      ['Notwaza', 641]
                    ])

annotation = Annotation("../../input/images/smash_senjou_test_0/resize2", "../../output/texts/smash_senjou_test_0/", waza_list)
annotation.annotation_main_test()

# リサイズ
resize = Resize("../../input/images/tilt_senjou_test_0/resize", "../../input/images/tilt_senjou_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 152], ['U-tilt', 201], ['Notwaza', 227], 
                      ['F-tilt', 268], ['Notwaza', 286], ['D-tilt', 326],
                      ['Notwaza', 398], ['U-tilt', 444], ['Notwaza', 454],
                      ['F-tilt', 498], ['Notwaza', 514], ['D-tilt', 554],
                      ['Notwaza', 590]
                    ])

annotation = Annotation("../../input/images/tilt_senjou_test_0/resize2", "../../output/texts/tilt_senjou_test_0/", waza_list)
annotation.annotation_main_test()

# リサイズ
resize = Resize("../../input/images/jabDa_senjou_test_0/resize", "../../input/images/jabDa_senjou_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 110], ['DA', 152], ['Notwaza', 184], 
                      ['DA', 224], ['Notwaza', 266], ['Jab1', 278],
                      ['Jab2', 314], ['Notwaza', 332], ['Jab1', 342],
                      ['Jab2', 382], ['Notwaza', 434]
                    ])

annotation = Annotation("../../input/images/jabDa_senjou_test_0/resize2", "../../output/texts/jabDa_senjou_test_0/", waza_list)
annotation.annotation_main_test()

# リサイズ
resize = Resize("../../input/images/grab_senjou_test_0/resize", "../../input/images/grab_senjou_test_0/resize2")
resize.resize()

waza_list = np.array([['Notwaza', 128], ['Grab', 177], ['D-throw', 215], 
                      ['Notwaza', 367], ['Grab', 406], ['U-throw', 455],
                      ['Notwaza', 631], ['Grab', 660], ['U-throw', 709],
                      ['Notwaza', 839], ['Grab', 863], ['D-throw', 899],
                      ['Notwaza', 1053], ['Grab', 1067], ['Grab-blow', 1205],
                      ['Notwaza', 1313], ['Grab', 1327], ['Grab-blow', 1477],
                      ['Notwaza', 1657], ['Grab', 1687], ['F-throw', 1713],
                      ['Notwaza', 1887], ['Grab', 1903], ['F-throw', 1929],
                      ['Notwaza', 2070], ['Grab', 2092], ['B-throw', 2121],
                      ['Notwaza', 2325], ['Grab', 2341], ['Grab-blow', 2361], ['B-throw', 2391],
                      ['Notwaza', 2567]
                    ])

annotation = Annotation("../../input/images/grab_senjou_test_0/resize2", "../../output/texts/grab_senjou_test_0/", waza_list)
annotation.annotation_main_test()

# # ここからステージ変更のプログラム(ヨッシーのみのマスク画像)

# backgroundChange = BackgroundChange("../../output/images/B-air_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/B-air_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/B-throw_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/B-throw_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/D-air_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/D-air_0/senjou")
# backgroundChange.run()

# # backgroundChange = BackgroundChange("../../output/images/D-smash_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/D-smash_0/senjou")
# # backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/D-throw_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/D-throw_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/D-tilt_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/D-tilt_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/DA_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/DA_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/Down-B_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/Down-B_0/senjou")
# backgroundChange.run()  

# backgroundChange = BackgroundChange("../../output/images/F-air_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/F-air_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/F-smash_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/F-smash_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/F-throw_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/F-throw_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/F-tilt_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/F-tilt_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/Grab-blow_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/Grab-blow_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/Jab_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/Jab_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/N-air_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/N-air_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/NB_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/NB_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/Side-B_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/Side-B_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/U-air_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/U-air_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/U-smash_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/U-smash_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/U-throw_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/U-throw_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/U-tilt_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/U-tilt_0/senjou")
# backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/Up-B_0/only_mask_resize", "../../input/images/stage/resize/senjou.png", "../../output/images/Up-B_0/senjou")
# backgroundChange.run()

# ここから画像の結合

resize = Resize("../../output/images/B-air_0/mask", "../../output/images/B-air_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/B-air_0/only_mask_resize", "../../output/images/B-air_0/mask_resize_kavi", "../../output/images/B-air_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/B-throw_0/mask", "../../output/images/B-throw_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/B-throw_0/only_mask_resize", "../../output/images/B-throw_0/mask_resize_kavi", "../../output/images/B-throw_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/D-air_0/mask", "../../output/images/D-air_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/D-air_0/only_mask_resize", "../../output/images/D-air_0/mask_resize_kavi", "../../output/images/D-air_0/conbination_mask")
combination.combine_images()

# resize = Resize("../../output/images/D-smash_0/mask", "../../output/images/D-smash_0/mask_resize_kavi")
# resize.resize()

# combination = Combination("../../output/images/D-smash_0/only_mask_resize", "../../output/images/D-smash_0/mask_resize_kavi", "../../output/images/D-smash_0/conbination_mask")
# combination.combine_images()

resize = Resize("../../output/images/D-throw_0/mask", "../../output/images/D-throw_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/D-throw_0/only_mask_resize", "../../output/images/D-throw_0/mask_resize_kavi", "../../output/images/D-throw_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/D-tilt_0/mask", "../../output/images/D-tilt_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/D-tilt_0/only_mask_resize", "../../output/images/D-tilt_0/mask_resize_kavi", "../../output/images/D-tilt_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/DA_0/mask", "../../output/images/DA_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/DA_0/only_mask_resize", "../../output/images/DA_0/mask_resize_kavi", "../../output/images/DA_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/Down-B_0/mask", "../../output/images/Down-B_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/Down-B_0/only_mask_resize", "../../output/images/Down-B_0/mask_resize_kavi", "../../output/images/Down-B_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/F-air_0/mask", "../../output/images/F-air_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/F-air_0/only_mask_resize", "../../output/images/F-air_0/mask_resize_kavi", "../../output/images/F-air_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/F-smash_0/mask", "../../output/images/F-smash_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/F-smash_0/only_mask_resize", "../../output/images/F-smash_0/mask_resize_kavi", "../../output/images/F-smash_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/F-throw_0/mask", "../../output/images/F-throw_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/F-throw_0/only_mask_resize", "../../output/images/F-throw_0/mask_resize_kavi", "../../output/images/F-throw_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/Grab-blow_0/mask", "../../output/images/Grab-blow_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/Grab-blow_0/only_mask_resize", "../../output/images/Grab-blow_0/mask_resize_kavi", "../../output/images/Grab-blow_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/Jab_0/mask", "../../output/images/Jab_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/Jab_0/only_mask_resize", "../../output/images/Jab_0/mask_resize_kavi", "../../output/images/Jab_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/N-air_0/mask", "../../output/images/N-air_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/N-air_0/only_mask_resize", "../../output/images/N-air_0/mask_resize_kavi", "../../output/images/N-air_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/NB_0/mask", "../../output/images/NB_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/NB_0/only_mask_resize", "../../output/images/NB_0/mask_resize_kavi", "../../output/images/NB_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/Side-B_0/mask", "../../output/images/Side-B_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/Side-B_0/only_mask_resize", "../../output/images/Side-B_0/mask_resize_kavi", "../../output/images/Side-B_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/U-air_0/mask", "../../output/images/U-air_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/U-air_0/only_mask_resize", "../../output/images/U-air_0/mask_resize_kavi", "../../output/images/U-air_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/U-smash_0/mask", "../../output/images/U-smash_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/U-smash_0/only_mask_resize", "../../output/images/U-smash_0/mask_resize_kavi", "../../output/images/U-smash_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/U-throw_0/mask", "../../output/images/U-throw_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/U-throw_0/only_mask_resize", "../../output/images/U-throw_0/mask_resize_kavi", "../../output/images/U-throw_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/U-tilt_0/mask", "../../output/images/U-tilt_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/U-tilt_0/only_mask_resize", "../../output/images/U-tilt_0/mask_resize_kavi", "../../output/images/U-tilt_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/Up-B_0/mask", "../../output/images/Up-B_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/Up-B_0/only_mask_resize", "../../output/images/Up-B_0/mask_resize_kavi", "../../output/images/Up-B_0/conbination_mask")
combination.combine_images()

resize = Resize("../../output/images/F-tilt_0/mask", "../../output/images/F-tilt_0/mask_resize_kavi")
resize.resize()

combination = Combination("../../output/images/F-tilt_0/only_mask_resize", "../../output/images/F-tilt_0/mask_resize_kavi", "../../output/images/F-tilt_0/conbination_mask")
combination.combine_images()

# カービィも含めた画像の作成

backgroundChange = BackgroundChange("../../output/images/B-air_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/B-air_0/senjou2")
# backgroundChange.stage_resize()
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/B-throw_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/B-throw_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/D-air_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/D-air_0/senjou2")
backgroundChange.run()

# backgroundChange = BackgroundChange("../../output/images/D-smash_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/D-smash_0/senjou2")
# backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/D-throw_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/D-throw_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/D-tilt_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/D-tilt_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/DA_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/DA_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/Down-B_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/Down-B_0/senjou2")
backgroundChange.run()  

backgroundChange = BackgroundChange("../../output/images/F-air_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/F-air_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/F-smash_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/F-smash_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/F-throw_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/F-throw_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/F-tilt_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/F-tilt_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/Grab-blow_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/Grab-blow_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/Jab_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/Jab_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/N-air_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/N-air_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/NB_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/NB_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/Side-B_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/Side-B_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/U-air_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/U-air_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/U-smash_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/U-smash_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/U-throw_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/U-throw_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/U-tilt_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/U-tilt_0/senjou2")
backgroundChange.run()

backgroundChange = BackgroundChange("../../output/images/Up-B_0/conbination_mask", "../../input/images/stage/resize/senjou.png", "../../output/images/Up-B_0/senjou2")
backgroundChange.run()