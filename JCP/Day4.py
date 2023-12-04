example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

my_puzzle = """
Card   1: 52 74  9  7 90 77 55 97 31 66 | 29 80 38 92 54 28 36 17 81 19 96 24 64 90 69 86 37  1 94 31 13 84 23 68 58
Card   2: 19 94 92 73 38 36 84 56 77 11 | 45  2 20 81 76 48 65 42 44 71 59 39 75 37 83 29 52 78 70 87 54 64 47 63 74
Card   3: 91 11 74 58 59 60 50 44  2 14 | 53 94 58 35 73 80 71  9 74 44 66 40 95 50 42 91  2 24 60 59 11 14 37  5 45
Card   4: 65 93 62 18 29 95  8 79 60 16 | 78 62 68  4 96  8 57 95 79 75 72 60 74 16 55 39 76 71 65 18 53 93 28 90 29
Card   5: 98 19 69 18 44 42 74  8 64 90 | 14 49 90 75 53 42 19 64 39 43  8 28 96 81 50 67 74 21 29  1 45 69 98 68 89
Card   6: 98 60 96 86 73 55 89 59 68 51 | 91 55 60 79 56 23 98 28 99 89  1 49 25 32 29 27 50 86 96 30 59 24 65 53 41
Card   7: 19  4  6 90 97 27 28 55 23 41 | 11 37 21 63 56 53  5 38 74 44 31 68 54  3 35 25 71 58  2 66  9 87 30 67 86
Card   8: 48 59 27  1 38 92 65 44 80 87 |  1 92 38 44 18 46 80 59 87 48 67 81 10 71 36 34 89 27 23 33 88 84 83 16 65
Card   9:  4 34 45 89 63 72 25 19 29 55 | 49 55 24 29 35 15  4 81 91 13 14 58 72 65  6 78 25 19  7 89 82 63 34  8 71
Card  10: 34 82 81 66 98 67 52 96 39 94 | 79  5 46 81 76 16 65 26  7 94 62  2 96 10 39 67 73 25 85 15 66 98 47 52 50
Card  11: 73 99 27 43 66  1 61 90  3 40 | 72  2 21 61  7 15 11 23 94 24 10 64 17 55 70 97 28 51 62 58 46 93 99 80  1
Card  12: 52 14 64 38  6 43  9 36 40 18 | 54 22  4 35 70 61 95  9 34 84 68 12 56 74 53  5 64 21 18 51 27 52 80 36 28
Card  13: 72 29 63 45 98 17 35 68 25 30 | 59 12  2 19 26 54 44 58 83 38 64 87 49 42 36 23 80 20 57 76 84 24  4 81 95
Card  14: 96 61 86 27 95 67 88  8 43 50 | 61 81 29 59 41 62 44 13 12 98 85 50 56 34 94  7  9 52 40 95  1 64 68 70 23
Card  15: 82 25 71 35 10 14 85 92 57 79 | 56 69  8  5 47 96 23 41 90 38 58 13 26  9 86 21 43 40 18 51 73 55 60 45 54
Card  16: 12  8 92 93 48 78 80 74 23  4 | 78 48 91 31 33 26 56 46 63 72  2 69 10 13  7 75 74 53 85 68 24 32 19 90 96
Card  17: 74 17 98 47 85 26 62 92 23 12 |  7 88 86 56 38 83  6 52 44 10  9 65 79 82 39 74 19 20 98 75 66 16 90 51 42
Card  18: 42 96 97 43 63 58 99 67 12 41 | 81 32 68 30 23 22 83 48 91 11 27 52 40 66 16 77 84 95 57 45  3 89 78 61 79
Card  19: 70 42 54 89 28  7 50 29 56 82 | 93 94 53 65 44 48 62 60 52 40 41 90  9 12  6 21 49 69 37 79 14 20 34 30 92
Card  20: 64 75 59 36 88  3 94 35 97 85 | 97 85 83 48 62 94 36 51 50 35 54  8 59 47 17 88  4  9 19 55 64 25 33  3 75
Card  21: 70 39 60 45 84 29 58 22 67  5 | 43 42 95 20 94 40 49 72 15 50 57 98  4 46 36 61 23  7 96 62  3 44 26 53 63
Card  22: 94  5 79 30 17 69 84 37 50 61 | 14 51 16 79 18 71 30 17 29 94  8 52 23 34  6 54 37 50 91 39 11 69 27 63  5
Card  23: 76 39 11 99 44 66 91 63 82 64 | 11 18 42 64  8 52 36 56 63 38 44  3 89 93 66 39 33 46 53 47 74 76 23 82 99
Card  24: 29 83 18 27 66 46 35 47 73 34 | 79 27 24 47 29 40 58 46 83 35 55 18 26 82  6 93 90 34 73 51 11 62 88 20 61
Card  25:  1 58 97 32 50  7 36 19 95 67 | 25 15 65  1 22 68 47 81 31 59 54 19 16 77 93 95 46 34 97 37 88 10 26 91  9
Card  26: 30 86 35 23 47 92 80 81 59 24 | 69 88 51 99 47  3 78 77 85 91 42 93 63 46 60 45  2 15 22 26 50 39  4 55 66
Card  27: 55 78 93  6 53 68 19 24 69 89 | 90 99 60 56 33 69 20 59 39 58 21 98 63  8  2 82 73 41 93 30 49 62 16 61 66
Card  28: 61 42 67 93 50 17 33 59 82 94 |  9 59 20 11 95  2 86 68 23 67 14 15 69 70 62 37 27 45 88  4 72  3 92 54 38
Card  29: 91 14 64  4 92 82  1 85 95 79 | 51 67 15 64 92 45 18 40 46 82 29 21 27  6 83  3 71 47 38 69 43 72 81 39 25
Card  30: 66 67 50 89 76 78 22 42  5 74 | 54 85  4 44 88 13 40 11 73 42 10  9 37 61 16 94 52 75 51 96 80 20 70  2 14
Card  31:  2 38 33 28 90 79  1 72 56 88 | 68  9 79  3 36 43 11  4 84 12 77 81 90 17 91 23 75 89 14 13 30 22  6 82 53
Card  32: 18 27 87 86  3 14 12 23 88 89 |  2 81 24 37  8 15 59 26 52 84  3 38 56 60 48 33 65 96 94 58 50 74 91 76 75
Card  33: 42 51 72 50 34 20 56 39  1 73 | 61 15 77 23 94 54 74 21 98 46 66 22 28 59 19 62 31 71 13 37 86 29  6 88 34
Card  34: 53 72 20 46 45 75 29  9  1 39 | 59 85 68 73  6 97 36 62 89 54 51 19 38 57  4 16 86 56  2 60 84 43 81 13 83
Card  35: 37 76 95 22 24 62 90 85  4 56 | 98 86 79 28 84 46 69  1 59  7 33 73 66 34 53 35 45 51 20 44 82 70 94 88 48
Card  36: 55 20 44 24 36 90 69  7 94 45 | 54  4 28 80 81 45 91 79  5 33 38 75 25 95 43 36 98 35 32 77 92 67 89 68 93
Card  37: 54  5 22 50  1 91 36 76  9 44 | 49  4 69 44 54 68  9 27  8 12 22 36 26 78  2 63 77 91  5 25 75 70 76  1 50
Card  38: 20 10 42 36 91 74 26 22 34 24 | 20 10  2 34 76 47 81 42 91 30 22 41 93 26 24 74 66 89 51 11 36 58 61 71 72
Card  39: 70 96 81 60 30 58 82  4 18 68 | 71 14 83 67  8 68 82 93  4 96 23 75 30 53 58 72 81 54 60 38 70 21 18  9 79
Card  40:  2 16  7 71 66 14 21 19 44 53 | 72 43 12 90 44 29 56  9 71 80 83 82 93 18 59 53 40 16 31 10 28 85 47 35 19
Card  41: 44  6 88 30 28 23 70 87 60 78 | 11 33 82 90 44 21 73  1  3 20 86 81 49 42  9 89 34 37 26 25 80 27 99 75 13
Card  42: 41 57 22  6 70 18 92 77  8 68 | 85 70 41 54 83 34 56 69 46 95 77 10 98 18  8 79 92 25 68 53 22 16 28  6 57
Card  43: 86  7  8 54 26  2 36 43  6 19 | 22  6 19 83 86 31 34 47 68 11 71 51  5 74  7 20 41  8 66  1 36 56  2 89 90
Card  44: 81 68 49 61 10 12 94 37 36 87 | 71 45 70 63 60 14  2 96 36 78 84 22 40  4 49 18 65 34 10 31 50 23 27 92 54
Card  45: 49 46 66 23 38 48 43 25 26 45 | 55 54 96 61 66 56 76 49 48  6 70 83 78 95 36 21 37 38 41 65 73 77 14 90 42
Card  46: 94 66 83 27 88 48 42 51 57 76 | 53 43 63 10 17 91 22 54 52 31 73 95 21 15 56 74 28  1 81 49  5 89  6 29 33
Card  47: 63 15 82 24 97  1 19 66 83 60 | 96 68  5 47 52 33 45 37 29 26 88  7 28 62 36 50 23 49 20 18 57  9 99 64 76
Card  48:  4 93 21 69 82 15  8 29 44 77 | 27 33 60 29 71  8 78 35 18 28 73 51 68 96 42 93 89 32 77 94 37 16 87 44 64
Card  49: 39 56 42 26 51 78 58 54 23 22 | 58 83 11 65 31 41  8 16 35 82 80 94 40 71 19 14 18 27 57 17 86 62 48 81 97
Card  50: 75 50 11 85 66 77 31 10 72 64 | 45 19 99 22 78 64 28 38 17 18 79  2 52 69 32 33 82 75 95 98 53 30 11 93 84
Card  51: 96 85 94  4 84 81 29 95 15 64 | 63 13 37 21 65  6 55 58 87 16 41 92 44 62 60 64 88 89 98 75 78  2 24 80 50
Card  52: 46 17 35 25 43  3 10 15 13 34 | 84 27 58 61 73 40 39 80 53 67 26 87  6 79 75 74 98 93 36 43 16 45  8 94 62
Card  53: 94 90  4 16 18 45 92 56 13 29 | 78 24 55 60 71 35 84  5 97 34 23 28 59  7  9 83  1 53 67 47 22 21 51 72 61
Card  54: 32 53  4  1 48 76 45  5 66 72 | 87  7 67 80 99 82 12 43 52 70 71 86 35 19 89 44 88 94 54 20 47 17 36 81 25
Card  55: 76 52 72 90 67 39 20 10 64 36 | 90 52 34 42 20 60 71 96 76 39  6 36 56 72 98 15 29 26 67 43 31 64 62 53 10
Card  56: 13 99 79 85 16 34 14 20 59 47 | 16 49  6 59 47 15 64 79 34 29  1 85 95 39 36 99 17 23  3 74 42 56 20 60 66
Card  57: 37 41 71 65 46 33 59 63 56 14 | 62 61 13 77 92 12 18 26 28  2 55 32 39 98 38 65 17 75 52 95 86 91  9 24 80
Card  58: 98 60 74 31 89 73 45 72 82 23 | 86 77 57 67 46 25 97 84 15 88  2 76 55 80  3 50 81 87  9 83 47 37 94 29 91
Card  59:  1 88 97 58 64 68 32 78  5 38 | 97 48 64 70 45 50 62 26 89  5 69 68 49 30  1 38 58 20 78 88 95  4 24 17 32
Card  60: 78 35 90 23 37 42 63 88 85 27 | 19 69 13 88 94 23 86 14 32 79 40 44 65  9 56 96 20 46 72 37 66 91 16 99 36
Card  61: 96 26 23 45 93 43 33 74 94 68 | 31 52 68 11 40 74 89 64 93 17 79 20 12 75 45 41 30 36 33 26  8 96 43 94 23
Card  62:  4 90 80 61 46 77 45 55 67 19 | 46 13 55 26 83 45 48 31 77 47  3 60  4 12 87 43 95 66 19 80 62 79  2 86 41
Card  63: 18 22 54 59 67 66 60 75 73 55 | 89  9 52 47 94 48 28 92 64  7 78 91 10 96 51 43 80 25 38 69 36 53 29 39 74
Card  64: 85 71 18 89 57  5 92 68 27 54 | 19 42 11 61 51  7 70 21 31 33 55 75 81 84 78 76 32  4 13 50 16 40 62 34 67
Card  65: 33 27 12 51 35  6 55 20 39 70 | 28 26 18 63 64 33 44 91 69 29 95  9 98 93 81 11 97  6 16 55 21 24 87 58 67
Card  66: 29 54 34 77 18 95 64 55 58 31 | 40  8 46 97 77 13 26 83 75 79 85 51 76 73 62 59 30 16 66 24 38 84 72 12 89
Card  67: 99 73 43 70 13  9 41 67 56  8 | 65 95 31 32 57 83 14 63 90 54 66  2 94 50 16 48 18 78 12 92 24 59 42 55 71
Card  68: 48 12  4 93  7 39 35 15 63 64 | 26 33 83 65 12 20 66  3 54  1 79 84 52 71 95 58 47 41 38 94  7 74 87 91  6
Card  69: 95 65  2 85 25 40 66 46 94 43 | 17 71  1 31 79 37 89 63 78 80 58 98 69 36 72 43 13 22 77 61 44 19 75 21 55
Card  70:  7 58 81 47 59 48 55 23 27 15 |  5 53 65 78 76 61 36 87 56 34 54 20 12 14 63 69 43 52 38 21 77  8 88 46 22
Card  71: 55 12 67 40 64 24 52 89 71 60 | 11 79 88 55 86 87 38 41 10 39 65 31 56 93 26 50 16 83 48 78 68 28 58 15 53
Card  72: 45 49 37 11 34  1 70 51 50 89 | 84 83 61  3 62 59 17 68 56 44 29 79  5 80 38 23 85 32 21 12 90 16 88 25 35
Card  73: 11 66 59 76 82 49  8 51 46 85 |  4 94 48 79 63 16 55 42 92 37 86  9 60  3 88 20 73 52 15 64 81 44 68  2 33
Card  74:  9 93 11  3 89 34 27 61 60 22 | 18 60 95 28 38 52 93 22 69 29 74  1 64 88 32 89 11 44 34  3 67 58 91 27 96
Card  75: 11  9 28 76 23 59 77 74 72  3 | 49 33 68 87 21 84 60 71 43 99 62 22 45 46  7  1  8 10 98 37 73 19 70 76 36
Card  76: 33 60  6 61 70 79 99 93 53 11 | 40 66 53 45 93 27 37 84 92 83 41 94 79 85 21 70 54 61  1 60 75 99 30 23 12
Card  77: 40 91 26 33 28 72 62 19 78 65 |  3 77 94 46 68 59 16 74  5 29 93 95 73 83 67 55 42 17 28 39 20 45 87 96  4
Card  78: 10  9  1 98 46  4  6 60 81 51 |  7 19 44 65 71 70 39 49 15 81 60 42  8 77 88 59 34 75 12 76 61 45 14 78 67
Card  79: 14 32 88  4 17 99 76 25 69 47 | 93 25  3 50 33 26 91 22 52 73 32 81  6  1 75 18 78 99 41 85 56 39 87 76 89
Card  80: 87 72 51 62 48 83 63 66 18 77 | 50  2 75 41 46 40 14 30 67 22 85  7 37 13 28 24 54 63 51 20 68 74 77 99 27
Card  81: 46 95 97 45 55 58 83  9  6 72 |  9 58 93 48 50 72 98 84 39 30  6 74 97 62 96 45  4 95 25 70 42 88  7 87 28
Card  82: 32 71  9 96 21 92 63 53 11  1 | 24 58 82 21 25 66 42 91 14 54 72 53 83 48 35 19 36 50 69 55 59  8 32 40 73
Card  83: 70 59 94 56 19 95  7 99 41 12 | 50 34 33  9 97 69 66  1 45 29 85 55 44  6 42  3 91 10 53 26 64 12 14 18 70
Card  84: 30 75 50 77 24 33 72 94 45 89 | 92  1 80 72 62 54 52 10 75 16 18 98 23  5 24 14 49 79 67 43 71  3  7 34 20
Card  85: 20 40 85 60 98 56 50 73 15 26 | 87  3 64 79  6 36 88 18 51 40 22 45 90 37 34 73 17 15 16 72 28 32 97 95 54
Card  86: 50 12 75  2 87 15 46 51 41 19 | 72 31 76  6 38 62 73 59 55 84 33 71 29 34 85 56 24 23 28 27 99 17 35 39 21
Card  87: 23  3  4 38 70 34 62 58 26 55 | 32 13 51 12 52 30 17 36 15 42 73 35 19 28 69 85 31 44 97 72 48 92 63 25 83
Card  88: 60 97 76 36 15 39 18  1 80 47 | 69 54 46 11 21 67 32 77 91 17 87  3 61 24 57 85 99 51  6 41 95  5 89 66  2
Card  89: 97 21 51  1 63 17 54 58 73 87 | 17 57 51 73 87 41 21 58 91 22 39 63 32 48 95 96 23 15 64 97 54 75 16  1 68
Card  90: 42 84 17 23 25 12  6 40 47 86 | 12 17 23 96 40 86 44 42 47 11  9 69 67 92 58  5 51 25 76 84  6 91 31 64 60
Card  91:  2 10 52 71  6 46 17 86 49 93 | 32 52 73 41 21 59  1 94 79 77 12 46 74 63 33 88 17 38 86 53 90 68 44 25 18
Card  92:  5 20 99  6 16 23 38 76 57 95 | 69 67 44 71  7 35 21 76 66 77 38 73 57 37 24 80 23 52 20 12 99 70 16 11  6
Card  93: 96 34 99 41 22  3 12  7 26 89 | 86 32 29 79 77 45 48  3 59 99 56 76 72 12 28 18 13 37 57 66 24 21 14  8 97
Card  94: 27 59 12 66 33 26 89 85 34 39 | 39 43 61 31 81 71 48 99 30 60 91 13 78 94 14 63 42 54 87 11 12 32 38  6 22
Card  95: 67 36 20 69 82 25 38 89 21 88 | 67 81 11 76 25 47 21 20  5 82 66 95 36 55 65 30 91 46 88 14 89 38 69  3 80
Card  96: 18 66 93 29 27 84 76  2  9 62 | 66  9 27 93 28 12 82 70  2  8 62 59 30 76 29 55 17 84 37 90 18 41 77 81 92
Card  97: 11 12 15 77 64 94 27 39 88 16 | 18 64 54 93 27 29 39 11 12 86 16 46 79 88 51 80 58 99 13 26 15 72 77 94 87
Card  98: 46 58 59 34 88 90 26 74 51  3 | 91 52 20 88 51 74 50 59 72 46 94 21 58 86  2 97 31 11 90 39 34 56 49 81 76
Card  99: 71 47 80 78 99 68 23 46 84  9 | 50  9 73 42  6 47 23 12 80 17 68 66 71  8 55 78 99 65 46 61 20 76 10 59 94
Card 100: 66  5 86 46 29 35  4 72 31 53 | 73 94 23  7 95 20 63 46 80 87 99 19 89 84 42  9 52 30 43 72 27 41 55  5 28
Card 101: 61  7 27 87 80 78 60 40 81 49 | 43 16 88 38 79 36 66 70 11 25 51 53 31 73 89 28  9 84 59 83 64 86 65  3 77
Card 102:  1 36 44 96  7 49 67  9 63 61 | 22 40 61 85  5 23 48  6 83 14 13 41 34 98 21 76 79  2 93 11 17 73 62 30 60
Card 103: 18 41 84 74 85 37 66 91 50 52 | 99 44 10 65 11 24 62 45 12  3 48  4 30 39 61 84 17 14 94 79 50 96 91 52 85
Card 104: 26 22 86  8 20 16  2 81 12 89 | 37 19 66 24 17 86 52 43 25 20 28 89 74 94 58 33 12 79 73 65  1 16 84  2 54
Card 105: 52  4 46 31 95 45 22  2 75 14 | 65 54 52 39 31 28 60 35 27 79 41 43 45 21  2 46 22 18 29 64 33 69 98 94 77
Card 106:  4 95 40 28 17 23 16 78 44 41 | 89 85 11 66 61 95 30 80  4 44 96 42  5 88  6 65 70 57  9 29 93 64 98 18 41
Card 107: 67 69 76 75 62 47 89 35 30 70 | 67 63 68 44 27 42 43 15 97 17  7 79 49 33  4 10 82 65 34 26 69  2 37 60 18
Card 108: 89 99 47 58 41 10 56 14 83 35 | 81 23 68 63 53 51 69 64 38 90 43 21 41 67 24 85 95 78  8  3 60 29 48 44 31
Card 109: 88 69 68 24 80 49 64  1 20 58 | 34 25 60 27 38 82  3 78 12 14 17 41 46 97 70 63 11 16 81 75 57  1 79 69 40
Card 110: 36 78 60  7  3 72 18  9 75 53 |  2 76 67 22 81 13 52 96 93 44 80 12 19 41  3 87 46 51 69 34 89 27 92 65 77
Card 111: 68  7 51 32 36 77 47  5 72 86 | 25 93 43 12 95  4 67 59 56 16 76 92  3 97 85 66 28 82 81 21 83 91 65 45 96
Card 112: 40 47 18 50 37 75 64 63  5 20 | 75 96 14 92 22 80 37 64 40 29 50 18 23 24 47 31 94  1 55 98 20 63 57 73 30
Card 113: 23 26 31 40 56 11  4 29 59 55 | 23 52 38 99 14 54 55  7 26 29 85 40  2 83 59 86  4 31 65  8 11 56 79 18 80
Card 114: 54 74 44 87 75 95 93 72 31 78 | 12 95 54 87 81 75 31 73 39 78 32 92 46 44 55  1 74 64 72  6  3 93 65 77 27
Card 115: 90 44 50 98 80 27 37 88 87  4 | 42 87 27 63 66 30 73  9 99 47 53 74 50 28  4 26 45 44 88 34  8 82 75 21  6
Card 116: 31 73 51 48 80 74 11 85 79 92 | 70 85 22 27 56 44 26 61 32 64 42 92 96 57 25 74 11 34 31 79 51 28 41  6 76
Card 117: 34 93 15 48 94 84 23 12 66 67 | 13 16  4 87 48 23 77 94 66 93 50 67 75 11 15 88 57 78 84 34 91 83  3 12 55
Card 118:  4 51 97 48 52 80 84 81 53 47 | 70 18 91 16 33 26  4 84 29 81 53 90 28 51 47 21 48 12 52 97 44 56 59 80 42
Card 119: 55 49 23 44 32 14 22 73 35  9 | 18 52 97 53 46 69  5  8 66 40 93 17 63 71 65  4 59 15 19 16 86 99 56 84 72
Card 120: 67  2 83 38 98 51  7 19 62 47 | 39 12 61 75  7 54 77 52 14 80 28 56 48 65 10 72 76 26 94 40 79 50 62 98 35
Card 121: 69 75 13 14 82 84 66 33 27 47 | 48 92 30 37 15 16 80 77 23 60 19 43 59 25 52 38  4 24 53 81 61 94 91 82 74
Card 122: 14 69 82 65 62 76 45 78 74 13 | 19 74 56 49 29 36  7 79 75 32 85 40 39 22 84 42 45 13 69 21 98  4 82 65 15
Card 123: 11 90 68 57 67  2 53 89 97 36 | 77 14 31 61 38 94 76 24 50 49 70 92 29 18 68 59 51  7 87  4 55 26  8 30 16
Card 124: 96 91 84 33 20 56  3  7  6 37 | 44 55 71 28 61 18 24 37 63 32 54 94 72 34 57 99 86 14 23 39 85 46 89 73 13
Card 125: 63 73  3 86  4 70 10 84 52 53 | 52 40  2 39 75 59 89 74 97 25 82 60  5 28 45 19 44 43 38 67 77 36 10 32 78
Card 126: 89 42 78  6 13 20 18 53 74 39 | 31 72 97 98  5 23 93 11 30  2 44 54 48 29 82 17 71 68 47 18 59 77 19 64 70
Card 127: 36 75  8 71 37  1  7 80 86 59 | 33 82 95  6 46 49 78 22 16 29 50 97 79 67 64 12 28  9 81 26 90 31 34 96 63
Card 128:  3  7 49 17 55 58 30  6 93 35 | 41 66 95 98 89 68 21 60 92 10 69  2 15 84 80  9 52 67 22 47 25 70 11 29 61
Card 129: 63 87 27 97 54  6 11 67 23 35 | 45 52 63  1  6 25 27 13 73 67 77 97 23 53 86 15 54 81 87 78 60 35 21 26 11
Card 130: 68 81 58  8 60 71 30 31 29 52 | 71 23 65 15 31 18 97 81 92 68 73 94 78 77  4 29 30 60  1  8 39 21 52 58 91
Card 131:  4 50  6 80 16 47 12 23 62 33 | 98 93  6 58 44 47 62 83  2 50  5 68 16 39 75 33 20 17 37 48 67 21 45 64 63
Card 132: 43 69 40 58 18 57 30 72 36  6 | 48 65 70 87 67  4 18 58 63 30 22 72 57 32 43 12 36 42  6 33 41 19 93 49 64
Card 133:  4 40 20 74 90 41 64 82  7 39 |  7 24 61 58 84 44 97 28 25 14 18 93 23 43 79 57 47 92 16 91 26 87 86 42 62
Card 134: 18 48 74 49 92 46 26 53 50 91 | 25 70 35 23 89 41 63 50 92 49 48 74 21 91 84 18 32  5 83 60 46 26 13 76 53
Card 135: 65  6 19 35 26 40  8 48 74 17 | 35 48 28 26 65  6 18 32  8 99 50 30 96 40 61 56  3 72 74 70 17 19  5 80 24
Card 136: 68 48 44 88 37  3 64 56 30 45 | 94 14 16 50 45 70 71 23 12 46 84 74 85 26 48 66 82 53 10 65 36 39 41 40 18
Card 137: 33 24 37 73 62 42 14 75 30 40 | 78 89 77 53 44 19 23 18 37 30 26 15 52 35 42 67 73 87  1 91 79 84 70 22  3
Card 138: 93 35 48 22 39  2 88 78 51 15 | 37 51 93 20 25 99 35 13 36 44 74 27 39 97 26 46  5 50 15 55 59 14 32 64 42
Card 139: 18 78 19 24 21 80 87 49 40 69 | 29 10  7  1  2 55 38 50 71 45 28 77 53 74 96 30 58 91 82 34 37 72 94 51 48
Card 140: 87 37 70 91  3 38 66 89 36 34 | 21 91 62 51 96 57 56 19 75  8  5 35 97 86 48 24 47 58 63 98 82 30 41 45 13
Card 141:  2 78 40  9 82 49 91  4 89 33 | 24 66 21 30 78 26  2 64 13 17 14 89 37 99 84 48 16 27 80 33 11 79 72  8 49
Card 142: 65 14 37 53 76 46 32  3 45 71 | 21 49 35 24 92 78 40 11 82 14 93 28 13 29 43  8 46 87 55  3 30 61  7 73 48
Card 143: 13 78 18 88 59 84 28 44 55 75 | 70 68 65 21 24 62 27 39 31 58 17 50 11  1 80 76 52 26  6 36 83 85 20 54 78
Card 144: 20 26 89 62 34 68 47 51 70 90 | 92 19 98 48 82 65 12 21 91 64 55  2 54  9 95  7 24 31 89 13  5 39 30 44 77
Card 145: 45 15 62 86 12 91 90 73 88 11 | 18 64 68 89 74 73 83 46 16 34 47 23 91 70 12 51 84 67 65 59 62  5 99 30 50
Card 146: 60 58 74 57 67 59 96 42  5 50 | 19 63 62 48 47 13  8 76  4 29 99 14 18 72 64 49 77 98 17 61 85 81 97 90 88
Card 147: 18 97 83 36  1 96 42 17 54 74 | 73 85  8 33 14 55  6 52 15 45 66 67 26  4 39 86 35 22 81 64  2 63 96  3 75
Card 148: 58 17 10 92  2 94 56 85 13 72 | 22 53 82 91 76 71 66 86 60 59 51 67 96 46 31 20 41 92 93 95 33 52 64  8 27
Card 149:  8 72 48 55 10 91 13 56 22 41 | 59 39 19 36 27 81 21 29 74 38 37 85  4 92 94 80 65 14 35 15 48 89 49 46 43
Card 150: 76 18 78 99 20 65 63 10 89 35 | 79 11 16 87 17 39 74 77  6 51 70 34 19 92 50 29 84 91 73 94 68 59  5 22 57
Card 151: 34 12 88 71  2 94 74 50 70 38 | 79 38 71 33 94 44 40 90 45 50 72 67 54 10 37 12 34 29 91 88 87 74  3 70  2
Card 152: 29 84 53 70 94 99 16 47 64 65 | 96 47 67 76 74  7 83 23 10 73 52 24 54 86  9 93 11 89 82 95 38  3 18 17 84
Card 153: 74 68 29  4 33 55 77 95 39  7 | 63  9  4 33 53 44 68 66 95 64 39 91 65 29 62 30 77 14  1 36  7 74  5  3 67
Card 154: 59 60 74 61 44  1 99 63 55 48 |  8  7 48 29 89 68 49 37 55 57 74 56 50 14 53 51 35 64  9 92 94 88 60  3 80
Card 155:  3 24 63 13 75 94 60 42 57  2 | 65 63 34 31 80 10  6 52 51 57 94 42 49 12  4 60 24 99 75  2 91 11 79  3 13
Card 156: 73 79 47 97 78  4 34  9 59 42 | 99 63 33 80 29 81 11 55 96 90 36 94 39 64 52 66 42 47 78 92 85 88 16  8 76
Card 157: 32 36  5 96 46 84 72 57 69 39 | 65 83 75 53 43 37 93 33 21 60 24 35 50 66  4 26 85 19 34  1 57 59 13 52 18
Card 158: 11 77  2 42 17 74 55 40  3  5 | 24 99 87 15 61 68 31 62 75 82 32 16 88 35  7 30 70 69 29 65 86 22 59 57 28
Card 159: 62 50 33  3 79 94 73 69 81 45 | 48 33 54 15 81  8 79 86  3 43 50 94 62 93 42 98 46 60 73 52 45 51 69 95 39
Card 160: 11 25 31 53 95 73 17 27 37 86 | 35 57 48 55 30 63 92 46 64 95 29 45 93 86 17 19 65 88 67  9 34 25 60 11 51
Card 161:  7 67  6 71 80 36 18 53 72 51 | 95 62 76 57 69 20 74  1 11 53 27 68  9 29 23 16 14 30 25 51 43 46 59  2 37
Card 162: 20 56 92 97 85 72 45 54 23  4 | 45 83 18 27 78 95 98  3 77 53 19 32  4 10 96  7 11 35 91 24  5 56 34 87 38
Card 163: 17 94 57 63 85  8 66 76 90 96 | 87 66 74 25 44 85 83 33 72  3 46 47 82 40 17 29 18 27 95  2 42 68  4 59 50
Card 164: 73 87 12 17 77 59 84 93 53 45 | 25 15 39 92 94  2 28 71 19 11  7 22 68  5 78 23  9 70 99 69 13 50 86 65 82
Card 165: 44 59 13 60 94 92 23 20 53 83 | 30 93 96 23 75 94 70 54 12 84 79 89 45 52 91 37 71  1 22 14 68 65 26 72 86
Card 166: 51 39 12 95 90 14 21 60 28 67 | 21 49 48 12 72 97 43 75 79 51 39 94 18 28 40  5 91 31 36 93 19 78 41 54 90
Card 167: 88 60 92 78 72 91 82 67 58 16 | 28 60 92 83 95 72 88 27 16 38 99 40 54 13 82 18 65 43 68 17 10 35 77 78 48
Card 168: 53 35 62 50 71 90 25 73 76 55 | 45 97 18 38 61 88 68 94 30 46 24 29 42 54 14  6 73 10  9 37 16 32  5 76 22
Card 169: 48 65 45 32 91 87 14 84  1 41 | 81 87 49 33  8 31  9 44 16 29 17 35 88 63 14 53 48 13 45 23 93 84 57  5 71
Card 170: 88 91 13 54  6 69 52 47 10 11 | 39 51  1  8 63 29 91 70 54 45 19 90 78 87 46 11  3 33 58 80 34 42 85 56 75
Card 171: 51 96 37 38 27 91 99 80 82  6 | 43 76 44 57 70 29 79 64 47 78 34 88 75 40 72 54 13 71 73 77 90 33 87 61 58
Card 172: 62 72 15  6 71 27 90 84 28 10 | 54 83 86 18 44 63 59 78 34 24 39 87 30 66 52 48 26 50  5 11 93 37 73  4 69
Card 173: 35  5 55 63 69 49 13 36 86  8 | 44  3 17 76 88 81  9 30 52 33 41 15 63 21 56 43 90 87 53 48 59 50 61 42 77
Card 174:  3 91 78 95 97 34 90 74 67 96 | 71 54 52 64 44 21 15 19 94 14 55 29 36 45 85 30 63 24 73 25 72 11 17 38 58
Card 175:  8 15 91 29  4 40 96 65 33 22 | 74 44 53 10 77 75 15 96 29 56 55 58  6  5  8 31 26 16 90 65 24 38 18  9 92
Card 176: 93 56  5 63 13 30 79 71 50 10 | 88 10  1 41 73 30 94 50 63 56 55 57 71 79  5 84 72 87 54 82 49 93 44 29 13
Card 177: 86 43 69 52  7 54 97 61 51 36 | 36 54 43 51 86 47 66 97 29 48 61 18 34 69 67  7 30  5 87 21 79 52 40 53 73
Card 178: 16 27 55 15 91 44  2 72 36  3 | 19 41 78  2 53 18 79 21  6 27 56 36 91  3 44 55 25 24 72 38 74 16 59 33 14
Card 179: 98 68 95 38 58 55 80 53 91 59 | 83 58 31  4 38 80 92 71 81 95 53 12 65 91 49 14 85 99 59 69 54 87 43 98 68
Card 180: 46 83 13 25 75 27  5 42  6 95 | 13 25  2 54 66 57  5 61 48 81 95 27 64 70 63 83 46 99 75 84 24 42 31  6 11
Card 181: 18 49 34 55 21 13 78 73 35 80 | 77 20 58 75 53 42 72 39 30 59 11 48 62  3 27 17 90 10 56 63  1 94 74 69 41
Card 182: 50 77 56 95 52 83 39 59 31 24 | 39  2 52 91 19 90 95 31 88 54 71 83 47 72 56 85 43 77 63 15 50  5 59 24 33
Card 183: 33 94 68 47 20 12 41 11 95 51 | 66 17 29 21 50  5 19 46 30 51 82 62 49 59 25 72 36 37 14 65 67 44 31 24 27
Card 184: 33 20 54 48  3 73 15 59 27 74 | 83 59 63 20 24 18 27  4 95 33  2 84  9 13  3 56 30  8 54 73 80 74  1 15 48
Card 185: 33 13 39 14 18 54 94 35 19 45 | 35 33 63 50 44 34 83  6  7 71 23 59 19 51 29 17 12  5 80 98 15 21 46 42 97
Card 186: 53 42 94 79 25 85 70 81 84 64 | 60 66 53 79 25 68 52 13 10 70 94 42 64 84 55 99 22 85 81  7 93 26 76 30 58
Card 187: 55 39 25 83 62 20 15  3 60 53 | 39 88 68  3 92 60 25 18 46 40 81 12  1 53 83 15 55 21 62 35 82 52 58 24 41
Card 188: 38 45 98 47 49 23 74  5 33  2 | 77 75 45  2 69 13 48 43 23 33 38 59 78 25 57 27 93 70 51  5 97 58 71 94 72
Card 189: 46 94 26 36 25 59  5 28 81 44 | 46 28  9  6 36 60  3 23 10 44 85 61 59  2 99 15 42 47 81  5 11 25 12 26 94
Card 190: 17 26 94 50 43 18 52 97 45 19 | 56 13 53 88 17 14 76 79 78 39 25 28 37 41 77 67 66 31 96 15 38 51 42  1 23
Card 191: 35 14 42 56 63 82 18  5 51 20 | 97 66 75 22 59 67 56 79 81 35 26  8 84 62 77  6 38 72 36  5 16 73 12 98 33
Card 192:  2 66 23 90 87 53 63 89 80 30 | 60 83 49 81 17 75 58 19 12  3 26 85  6 89 74 57 55 61 56 41 79 91 59 27 96
Card 193: 29 91  7 78 39 34 69 32 81 56 |  5 28 34 12 62 85 31 50 22 55 29 32 91 63 11  2  7  8 98 19 15 90 56 97 66
Card 194: 33 39 63 20 34 51 36 52 11 87 | 98 51 78 43 93 19 36 26 79 28 87 68 70 10 57 82 89 63 91 58 48 30 22 41  2
Card 195: 81 52 44 89 35 22 17 87 64 99 | 18 16 95 32 39 15  7 70 21 25 72 55 88 80 13 96 81 46 92 33 58 99 57 45 24
Card 196: 66 76 14 62 42 89 60 70 37 35 | 25 49 97 34 42 60 91 68 40 50  6 17 63 93 27 57 62 44 48 29  9 46 94 88 87
Card 197: 62 33 96 37 22 14 49 27 39  6 | 94 97 85  5 57 48 64 38  8 71 79 19 65 82 50 78 52 13 92 62 72 27 28 21 80
Card 198: 69 41 63 28  9 10  3 64 87 57 | 19 78 88 38 29 54 93 76 22 36 86 20 61 53 66  4 77 67 85 11 27 94 43 74 90
Card 199: 88 39 24 36 67 97 72  9 13 30 | 17 12 16 38 89 64 99 96 79 84 81 11 90 21 76 91 78 42 50 18 48 62 58 59 63"""

def parse_input(input):
  cards = []
  for line in input.split("\n"):
    if line == "":
      continue
    cards.append([x.split(" ") for x in line.split(":")[1].strip().replace("  ", " ").split(" | ")])
  return cards

def part1(input):
  cards = parse_input(input)
  sum = 0
  for card in cards:
    winnings = [x for x in card[1] if x in card[0]]
    if winnings:
      sum += pow(2, len(winnings)-1)
  return sum

def part2(input):
  cards = parse_input(input)
  result = {x: 1 for x in range(len(cards))}
  for i in range(len(cards)):
    card = cards[i]
    winnings = [x for x in card[1] if x in card[0]]
    if winnings:
      for j in range(len(winnings)):
        result[i+j+1] += result[i]
  return sum(result.values())

print("Points for part1 example : " + str(part1(example)))
print("Points for part1 my input : " + str(part1(my_puzzle)))

print("Cards for part2 example : " + str(part2(example)))
print("Cards for part2 my input : " + str(part2(my_puzzle)))
