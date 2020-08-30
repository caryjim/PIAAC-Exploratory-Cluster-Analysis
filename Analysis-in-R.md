Exploratory Analysis of PIAAC in R
================
Cary K. Jim
June 2020

###### A python version of the analysis can be found on Github - [PIAAC-Exploratory-Cluster-Analysis](https://github.com/caryjim/PIAAC-Exploratory-Cluster-Analysis).

###### This work is part of an ongoing project which is accepted at the 2020 AERA Satellite Conference on Educational Data Science (Sept 18,2020).

``` r
library(foreign)
# Note: The arguments settings will import the numerical values, not the labels. 
usa <-read.spss(file = "prgushp1_puf.sav", use.value.labels = FALSE, to.data.frame=TRUE, use.missings = TRUE)
```

    ## re-encoding from CP1252

There is a package in R ,
[memisc](http://www.martin-elff.net/software/memisc/import/) that can
process the sav file. Ideally, we should import the spss raw data and
the metadata in two separate files. Here for simplicity, the foreign
package is used here to extract only the numerical values in the dataset
since we have the codebook for labels & levels identification. In the
Python version, pyreadstat can import and separate the metadata and raw
values in one line of code.

## Part 1: Data Preparation and Statistical summary

#### Create datasets from the usa file

``` r
# Create dataframes bases on desired variables
# Background variables, literacy scores, numeracy scores, and problem-solving scores (in technology rich environment)

bkg <- usa[, c("SEQID", "GENDER_R", "B_Q01A", "C_D05", "WRITHOME", "WRITWORK",
               "READHOME", "READWORK", "NUMHOME", "NUMWORK","ICTHOME", "ICTWORK")]
lit <- usa[, c('SEQID', 'PVLIT1', 'PVLIT2', 'PVLIT3', 'PVLIT4', 'PVLIT5', 'PVLIT6',
               'PVLIT7', 'PVLIT8', 'PVLIT9', 'PVLIT10')]
num <- usa[, c('SEQID', 'PVNUM1', 'PVNUM2', 'PVNUM3', 'PVNUM4', 'PVNUM5', 'PVNUM6',
               'PVNUM7', 'PVNUM8', 'PVNUM9', 'PVNUM10')]
psl <- usa[, c('SEQID', 'PVPSL1', 'PVPSL2', 'PVPSL3', 'PVPSL4', 'PVPSL5', 'PVPSL6',
               'PVPSL7', 'PVPSL8', 'PVPSL9', 'PVPSL10')]
```

##### Description of the variables

  - Participant ID : SEQID
  - Demographic Information:
      - Gender (GENDER\_R) 1.0 - Male, 2.0 - Female
      - Highest Education Levels Completed (B\_Q01A), ISCED Levels for
        US Data coded as:
      - 2: Grade 1-6; 3: Grade 7-9; 7: High School Diploma; 9: Cert.
        from trade school; 11: Associate Degree; 12: Bachelor Degree;
        13: Master Degree/Prof. Degree; 14: Doctorate Degree; 15:
        Foreign Qual.
      - Employment Status (C\_D05): 1.0 - Employed, 2.0 - Unemployed,
        3.0 - Out of Labor Force, 4.0 - Not Known: 4

There are standardized scales scores for skills use derived from items
in background survey \* Index of Reading Skills at Home or at Work
(Non-nested scales) + READHOME, READWORK: literacy skills for both
document and prose type texts \* Index of Writing Skills at Home or at
Work (Non-nested scales) + WRITHOME, WRITWORK: writing skills such as
writing letters, mails, articles, reports or fill in forms \* Index of
Numeracy Skills at Home or at Work (Non-nested scales) + NUMHOME,
NUMWORK: Numeracy activities such as calculation, prepare graphs/charts,
use formulas, or advanced math \* Index of ICT Skills at Home or at Work
+ ICTHOME, ICTWORK: Literacy(Digital Reading), using of computers and
internet for various tasks (mail, documents)

There are cognitive assessment scale scores for literacy test, numeracy
test, and problem solving test \* Literacy - plausible values: PVLIT1 to
PVLIT10 \* Numeracy - plausible values: PVNUM1 to PVNUM10 \* Problem
Solving in Technology Rich Environment: PVPSL1 to PVPSL10

#### Descriptive statistics

Background Variables

``` r
# summary () gives min, 1stQu, Median, Mean, 3rdQu, Max)
summary(bkg)
```

    ##      SEQID         GENDER_R         B_Q01A           C_D05      
    ##  Min.   :   1   Min.   :1.000   Min.   : 1.000   Min.   :1.000  
    ##  1st Qu.:2168   1st Qu.:1.000   1st Qu.: 7.000   1st Qu.:1.000  
    ##  Median :4336   Median :2.000   Median : 7.000   Median :1.000  
    ##  Mean   :4336   Mean   :1.537   Mean   : 8.139   Mean   :1.651  
    ##  3rd Qu.:6503   3rd Qu.:2.000   3rd Qu.:12.000   3rd Qu.:2.000  
    ##  Max.   :8670   Max.   :2.000   Max.   :15.000   Max.   :4.000  
    ##                                 NA's   :198      NA's   :189    
    ##     WRITHOME         WRITWORK        READHOME         READWORK      
    ##  Min.   :-0.296   Min.   :0.056   Min.   :-1.299   Min.   :-0.9555  
    ##  1st Qu.: 1.685   1st Qu.:1.266   1st Qu.: 1.967   1st Qu.: 1.4671  
    ##  Median : 2.530   Median :2.069   Median : 2.514   Median : 2.0571  
    ##  Mean   : 2.271   Mean   :2.124   Mean   : 2.485   Mean   : 2.0914  
    ##  3rd Qu.: 2.890   3rd Qu.:2.815   3rd Qu.: 3.002   3rd Qu.: 2.6654  
    ##  Max.   : 6.104   Max.   :5.800   Max.   : 7.427   Max.   : 7.0208  
    ##  NA's   :960      NA's   :3608    NA's   :279      NA's   :2840     
    ##     NUMHOME           NUMWORK          ICTHOME          ICTWORK     
    ##  Min.   :-0.5083   Min.   :-0.090   Min.   :-1.209   Min.   :0.009  
    ##  1st Qu.: 1.7752   1st Qu.: 1.547   1st Qu.: 1.585   1st Qu.:1.140  
    ##  Median : 2.4017   Median : 2.115   Median : 2.229   Median :1.855  
    ##  Mean   : 2.3384   Mean   : 2.170   Mean   : 2.196   Mean   :2.044  
    ##  3rd Qu.: 2.9535   3rd Qu.: 2.795   3rd Qu.: 2.808   3rd Qu.:2.769  
    ##  Max.   : 6.1737   Max.   : 6.050   Max.   : 7.710   Max.   :5.463  
    ##  NA's   :627       NA's   :3672     NA's   :1943     NA's   :4615

``` r
# describe() in psych gives n, mean, sd, meadian, trimmed, mad, min, max, range, skew, kurtosis, se
library(psych)

describe(bkg)
```

    ##          vars    n    mean      sd  median trimmed     mad   min     max
    ## SEQID       1 8670 4335.50 2502.96 4335.50 4335.50 3213.54  1.00 8670.00
    ## GENDER_R    2 8670    1.54    0.50    2.00    1.55    0.00  1.00    2.00
    ## B_Q01A      3 8472    8.14    3.25    7.00    8.18    2.97  1.00   15.00
    ## C_D05       4 8481    1.65    0.84    1.00    1.56    0.00  1.00    4.00
    ## WRITHOME    5 7710    2.27    1.00    2.53    2.36    0.70 -0.30    6.10
    ## WRITWORK    6 5062    2.12    1.11    2.07    2.10    1.16  0.06    5.80
    ## READHOME    7 8391    2.49    0.97    2.51    2.49    0.76 -1.30    7.43
    ## READWORK    8 5830    2.09    1.04    2.06    2.07    0.89 -0.96    7.02
    ## NUMHOME     9 8043    2.34    0.97    2.40    2.37    0.87 -0.51    6.17
    ## NUMWORK    10 4998    2.17    1.02    2.11    2.14    0.91 -0.09    6.05
    ## ICTHOME    11 6727    2.20    0.95    2.23    2.20    0.91 -1.21    7.71
    ## ICTWORK    12 4055    2.04    1.12    1.85    1.96    1.14  0.01    5.46
    ##            range  skew kurtosis    se
    ## SEQID    8669.00  0.00    -1.20 26.88
    ## GENDER_R    1.00 -0.15    -1.98  0.01
    ## B_Q01A     14.00 -0.06    -0.90  0.04
    ## C_D05       3.00  0.74    -1.17  0.01
    ## WRITHOME    6.40 -0.73     0.55  0.01
    ## WRITWORK    5.74  0.33    -0.13  0.02
    ## READHOME    8.73  0.41     3.96  0.01
    ## READWORK    7.98  0.63     2.82  0.01
    ## NUMHOME     6.68 -0.12     1.34  0.01
    ## NUMWORK     6.14  0.47     0.85  0.01
    ## ICTHOME     8.92  0.15     1.55  0.01
    ## ICTWORK     5.45  0.71     0.08  0.02

Numeracy, literacy, and problem solving plausible values from the
cognitive assessment part of PIAAC

``` r
describe(num)
```

    ##         vars    n    mean      sd  median trimmed     mad   min     max   range
    ## SEQID      1 8670 4335.50 2502.96 4335.50 4335.50 3213.54  1.00 8670.00 8669.00
    ## PVNUM1     2 8488  250.66   55.23  252.40  251.43   56.40 65.13  432.07  366.94
    ## PVNUM2     3 8488  250.35   55.35  251.51  251.08   56.64 39.69  438.64  398.95
    ## PVNUM3     4 8488  250.86   55.23  252.35  251.66   56.98 70.14  425.68  355.54
    ## PVNUM4     5 8488  250.54   55.19  252.17  251.52   57.11 57.18  429.04  371.86
    ## PVNUM5     6 8488  250.67   55.42  251.94  251.34   57.47 42.82  439.68  396.86
    ## PVNUM6     7 8488  250.61   54.91  251.86  251.40   56.07 52.27  436.09  383.82
    ## PVNUM7     8 8488  250.18   54.65  252.14  251.11   55.98 44.33  458.28  413.95
    ## PVNUM8     9 8488  250.68   54.53  252.82  251.65   55.49  0.00  424.23  424.23
    ## PVNUM9    10 8488  251.01   55.11  252.24  251.78   56.23 20.76  431.29  410.54
    ## PVNUM10   11 8488  250.35   54.78  252.46  251.33   56.75 67.64  445.03  377.39
    ##          skew kurtosis    se
    ## SEQID    0.00    -1.20 26.88
    ## PVNUM1  -0.13    -0.22  0.60
    ## PVNUM2  -0.13    -0.23  0.60
    ## PVNUM3  -0.13    -0.23  0.60
    ## PVNUM4  -0.16    -0.22  0.60
    ## PVNUM5  -0.11    -0.23  0.60
    ## PVNUM6  -0.13    -0.14  0.60
    ## PVNUM7  -0.14    -0.18  0.59
    ## PVNUM8  -0.18    -0.12  0.59
    ## PVNUM9  -0.14    -0.20  0.60
    ## PVNUM10 -0.16    -0.20  0.59

``` r
describe(lit)
```

    ##         vars    n    mean      sd  median trimmed     mad   min     max   range
    ## SEQID      1 8670 4335.50 2502.96 4335.50 4335.50 3213.54  1.00 8670.00 8669.00
    ## PVLIT1     2 8488  268.23   49.70  270.68  269.59   49.82 86.65  449.73  363.08
    ## PVLIT2     3 8488  267.44   50.12  269.05  268.77   49.81 43.05  429.63  386.58
    ## PVLIT3     4 8488  267.52   49.86  269.70  268.97   49.72 61.84  418.51  356.67
    ## PVLIT4     5 8488  268.21   49.02  270.70  269.60   49.59 95.64  429.96  334.32
    ## PVLIT5     6 8488  266.96   49.26  269.51  268.26   49.67 67.62  434.27  366.65
    ## PVLIT6     7 8488  267.83   49.22  270.19  269.22   49.80 39.71  425.01  385.30
    ## PVLIT7     8 8488  267.08   49.15  269.06  268.43   49.49 75.40  448.65  373.25
    ## PVLIT8     9 8488  267.12   49.75  269.96  268.69   49.34 66.48  425.98  359.51
    ## PVLIT9    10 8488  267.81   49.62  270.18  269.03   49.37 76.43  447.55  371.12
    ## PVLIT10   11 8488  267.62   49.14  269.98  269.09   49.14 76.60  430.91  354.31
    ##          skew kurtosis    se
    ## SEQID    0.00    -1.20 26.88
    ## PVLIT1  -0.28     0.06  0.54
    ## PVLIT2  -0.27     0.04  0.54
    ## PVLIT3  -0.28     0.02  0.54
    ## PVLIT4  -0.27    -0.08  0.53
    ## PVLIT5  -0.26    -0.02  0.53
    ## PVLIT6  -0.29     0.08  0.53
    ## PVLIT7  -0.25     0.04  0.53
    ## PVLIT8  -0.32     0.09  0.54
    ## PVLIT9  -0.26     0.08  0.54
    ## PVLIT10 -0.30     0.05  0.53

``` r
describe(psl)
```

    ##         vars    n    mean      sd  median trimmed     mad    min     max
    ## SEQID      1 8670 4335.50 2502.96 4335.50 4335.50 3213.54   1.00 8670.00
    ## PVPSL1     2 6880  270.04   43.70  271.39  270.90   44.99  93.90  416.48
    ## PVPSL2     3 6880  271.14   43.10  272.47  271.95   43.83  77.73  411.55
    ## PVPSL3     4 6880  270.68   44.08  272.62  271.60   44.18  78.27  432.25
    ## PVPSL4     5 6880  271.33   43.05  273.22  272.39   43.73  85.74  417.47
    ## PVPSL5     6 6880  270.63   44.59  272.35  271.62   45.01  98.63  425.95
    ## PVPSL6     7 6880  269.95   43.65  271.83  270.69   43.33  97.85  406.54
    ## PVPSL7     8 6880  270.42   44.09  272.11  271.26   43.65 111.26  415.39
    ## PVPSL8     9 6880  269.60   43.54  271.01  270.58   43.39  70.65  422.79
    ## PVPSL9    10 6880  270.52   43.67  272.75  271.42   42.56  93.88  440.36
    ## PVPSL10   11 6880  271.07   44.30  272.85  272.04   44.68  60.38  404.37
    ##           range  skew kurtosis    se
    ## SEQID   8669.00  0.00    -1.20 26.88
    ## PVPSL1   322.58 -0.19    -0.06  0.53
    ## PVPSL2   333.83 -0.22     0.08  0.52
    ## PVPSL3   353.98 -0.21     0.05  0.53
    ## PVPSL4   331.73 -0.24     0.00  0.52
    ## PVPSL5   327.31 -0.24     0.10  0.54
    ## PVPSL6   308.68 -0.17    -0.06  0.53
    ## PVPSL7   304.14 -0.20     0.00  0.53
    ## PVPSL8   352.14 -0.22     0.05  0.52
    ## PVPSL9   346.49 -0.22     0.13  0.53
    ## PVPSL10  343.99 -0.25     0.09  0.53

#### Correlation of background variables

``` r
# Calculate correlation with cor() in pearson r 
cor(bkg, use = "complete.obs", method = c("pearson"))
```

    ##                  SEQID    GENDER_R       B_Q01A       C_D05    WRITHOME
    ## SEQID     1.000000e+00 -0.03353248  0.007529388 -0.00618306 -0.01262527
    ## GENDER_R -3.353248e-02  1.00000000  0.014904222  0.03336976  0.04532127
    ## B_Q01A    7.529388e-03  0.01490422  1.000000000 -0.12360431  0.05154553
    ## C_D05    -6.183060e-03  0.03336976 -0.123604308  1.00000000  0.08773160
    ## WRITHOME -1.262527e-02  0.04532127  0.051545528  0.08773160  1.00000000
    ## WRITWORK -9.518651e-04 -0.04130268  0.172059970 -0.07322448  0.16500222
    ## READHOME -2.053379e-02 -0.07157384  0.063501025  0.06630679  0.44767004
    ## READWORK -4.901627e-03 -0.09789409  0.242715268 -0.09068269  0.15755140
    ## NUMHOME  -1.326147e-02 -0.09769995 -0.009190662  0.08305362  0.41137669
    ## NUMWORK  -7.034229e-05 -0.14747447  0.079065513 -0.04748671  0.12323758
    ## ICTHOME  -1.425721e-02 -0.05229241  0.218802300  0.03509562  0.45431744
    ## ICTWORK   1.265666e-03 -0.06151184  0.298905461 -0.09382628  0.13766438
    ##               WRITWORK    READHOME     READWORK      NUMHOME       NUMWORK
    ## SEQID    -0.0009518651 -0.02053379 -0.004901627 -0.013261466 -7.034229e-05
    ## GENDER_R -0.0413026820 -0.07157384 -0.097894094 -0.097699950 -1.474745e-01
    ## B_Q01A    0.1720599698  0.06350102  0.242715268 -0.009190662  7.906551e-02
    ## C_D05    -0.0732244843  0.06630679 -0.090682690  0.083053619 -4.748671e-02
    ## WRITHOME  0.1650022176  0.44767004  0.157551395  0.411376686  1.232376e-01
    ## WRITWORK  1.0000000000  0.17943583  0.459619182  0.080893291  3.132347e-01
    ## READHOME  0.1794358345  1.00000000  0.405006451  0.459973014  2.060986e-01
    ## READWORK  0.4596191819  0.40500645  1.000000000  0.141589923  3.453898e-01
    ## NUMHOME   0.0808932906  0.45997301  0.141589923  1.000000000  3.196964e-01
    ## NUMWORK   0.3132347402  0.20609855  0.345389760  0.319696384  1.000000e+00
    ## ICTHOME   0.2039486416  0.45789128  0.238029373  0.453556169  1.785235e-01
    ## ICTWORK   0.4727995411  0.17443037  0.453126466  0.117828528  3.660903e-01
    ##              ICTHOME      ICTWORK
    ## SEQID    -0.01425721  0.001265666
    ## GENDER_R -0.05229241 -0.061511837
    ## B_Q01A    0.21880230  0.298905461
    ## C_D05     0.03509562 -0.093826281
    ## WRITHOME  0.45431744  0.137664379
    ## WRITWORK  0.20394864  0.472799541
    ## READHOME  0.45789128  0.174430371
    ## READWORK  0.23802937  0.453126466
    ## NUMHOME   0.45355617  0.117828528
    ## NUMWORK   0.17852347  0.366090289
    ## ICTHOME   1.00000000  0.395642703
    ## ICTWORK   0.39564270  1.000000000

``` r
# Create a correlation table and round the values to 3 decimal places
cortable <- round(cor(bkg, use = "complete.obs", method = c("pearson")), 3)

# Plotting the correlation values with the corrplot
library(corrplot)
```

    ## corrplot 0.84 loaded

``` r
corrplot(cortable)
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-4-1.png)<!-- -->

#### Kernel Density Estimates of Continuous Variables in the Background dataset

##### Using Gaussian distribution for the KDE

``` r
a <- density(bkg$ICTHOME, na.rm = TRUE, kernel = c("gaussian"))  
plot(a, main = "Density Plot  of ICT use at Home Index")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-5-1.png)<!-- -->

``` r
b <- density(bkg$ICTWORK, na.rm = TRUE, kernel = c("gaussian")) 
plot(b, main = "Density Plot  of ICT use at Work Index")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-5-2.png)<!-- -->

``` r
c <- density(bkg$READHOME, na.rm = TRUE, kernel = c("gaussian")) 
plot(c, main = "Density Plot  of Read at Home Index")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-5-3.png)<!-- -->

``` r
d <- density(bkg$WRITHOME, na.rm = TRUE, kernel = c("gaussian")) 
plot(d, main = "Density Plot  of Write at Home Index")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-5-4.png)<!-- -->

``` r
e <- density(bkg$READWORK, na.rm = TRUE, kernel = c("gaussian")) 
plot(e, main = "Density Plot  of READ at Work Index")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-5-5.png)<!-- -->

``` r
f <- density(bkg$WRITWORK, na.rm = TRUE, kernel = c("gaussian")) 
plot(f, main = "Density Plot  of WRITE at Work Index")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-5-6.png)<!-- -->

``` r
g <- density(bkg$NUMHOME, na.rm = TRUE, kernel = c("gaussian")) 
plot(g, main = "Density Plot  of NUMHOME Index")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-5-7.png)<!-- -->

``` r
h <- density(bkg$NUMWORK, na.rm = TRUE, kernel = c("gaussian")) 
plot(h, main = "Density Plot  of NUMWORK Index")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-5-8.png)<!-- -->

The density function plots display several variables with multi-modal
distribution. This gives us a sense that for the available(excluding
missing) data of the participants in the PIAAC background variables,
there are subgroups with different levels of skills.

#### Charts for Categorical Variables

Gender, Gender by Edu level, Gender by Employment Status.

Note: These charts are different to the ones showed in the Python
version.

``` r
gender <- table(bkg$GENDER_R)
barplot(gender, names.arg=c("Male","Female"),
        ylim = c(0, 5000),
        col=c("blue","orange"),
        ylab="Count",
        main = "Gender")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->

``` r
# Gender by Education Level
EduLv <- with(bkg, table(GENDER_R, B_Q01A))
barplot(EduLv, beside = TRUE, ylim = c(0,2000), ylab="Count", 
        col=c("blue","orange"),
        xlab="Education Level- ISCED",
        legend.text = c("Male", "Female"),
        args.legend = list(x="topright"),
        main = "Gender by Education Level")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-7-1.png)<!-- -->

``` r
# Gender by Employment Status
Emp <- with(bkg, table(GENDER_R, C_D05))
barplot(Emp, beside = TRUE, names.arg=c("Employed","Unemployed", "Out of Labor Force", "Not Known"),
        ylim = c(0,2500), ylab="Count", 
        col=c("blue","orange"),
        xlab ="Employment Status",
        legend.text = c("Male", "Female"),
        args.legend = list(x="topright"),
        main = "Gender by Employment Status")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-8-1.png)<!-- -->

#### Charts for the cognitive assessment scores: literacy(lit), numeracy(num), and problem solving in technology rich enviornment(psl)

Since the plausible values of each assessment has been scaled, the
following charts are example of one plausible values (from the 10
plausible values) in each assessment.

``` r
hist(lit$PVLIT1, xlab = "Literacy Score Plausible Value 1 (PVLIT1)", main = "Histrogram of Literacy PVLIT1 Scores")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-9-1.png)<!-- -->

``` r
plot(density(lit$PVLIT1, na.rm = TRUE), xlab = "Literacy Score Plausible Value 1 (PVLIT1)", main = "Density Plot of Literacy PVLIT1 Scores")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-10-1.png)<!-- -->

``` r
hist(num$PVNUM5, xlab = "Numeracy Score Plausible Value 5 (PVLIT5)", main = "Histrogram of Numeracy Scores - PVNUM5")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-11-1.png)<!-- -->

``` r
plot(density(num$PVNUM5, na.rm = TRUE), xlab = "Numeracy Score Plausible Value 5 (PVNUM5)", main = "Density Plot of Numeracy Scores")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-11-2.png)<!-- -->

``` r
hist(psl$PVPSL10, xlab = "Problem Solving in TRE Plausible Value 10 (PVPSL10)", main = "Histrogram of PSTRE Scores - PVPSL10")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-12-1.png)<!-- -->

``` r
plot(density(num$PVNUM5, na.rm = TRUE), xlab = "PS-TRE Score Plausible Value 10 (PVPSL10)", main = "Density Plot of Problem Solving in TRE Scores - PVPSL10")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-12-2.png)<!-- -->

## Part 2: Clustering Analysis

There are few resources that inform this part of the R code development
and analysis. See References at the end.

``` r
# Merge Dataframes between background variables to each types of cognitive assessment scores

bkg_lit <- merge(bkg, lit, by = "SEQID")
bkg_num <- merge(bkg, num, by = "SEQID")
bkg_psl <- merge(bkg, psl, by = "SEQID")
```

##### The numeracy scores and the background variables are used for the following analysis

The bkg\_num dataset contains the demographic information, skill indexes
and the numeracy scores. Torgo (2017) suggested the use of daisy()
function in the cluster package to determine the dissimilarity matrix
with mixed types of variables.For k-mean analysis, only the continuous
variables are used in this example.

##### Further preparation of the dataset

For this analysis, we are only interested in adults who has been
assessed by the numeracy test and also have been responded to the
background questions of their skills used in reading, writing, ICT and
numeracy. After reviewing the [PIAAC Technical
Report](https://www.oecd.org/skills/piaac/_Technical%20Report_17OCT13.pdf)
and [PIAAC Household Sample
Codebook](https://nces.ed.gov/pubs2016/data/2016667REV_codebook.pdf),
the non-response or skipped participants missing values cannot be
estimated to properly reflect their characteristics. Therefore,
participants with missing values in the selected variables are dropped.

Also, this analysis is not inferential in nature, we are looking at
participants who responded to the survey items and have a valid scores
for the cognitive assessments. Futher reading of missing data in cluster
analysis can be found in Everitt, Landau, & Leese (2001).

``` r
# Drop SEQID (for participant ID), Gender, Edu level, and Employment status in bkg_num dataset
data <- as.data.frame(bkg_num[5:22])
# Move the SEQID, Gender, EDUlevel, and Emploment to anothe dataframe for later use
roster <-as.data.frame(bkg_num[1:4])
# Drop any missing values by rows
data <- data[complete.cases(data),]
```

Re-examine the data summary to visually inspect any large changes after
removal of missing values.

``` r
describe(data)
```

    ##          vars    n   mean    sd median trimmed   mad    min    max  range  skew
    ## WRITHOME    1 3300   2.45  0.86   2.63    2.52  0.57  -0.30   6.10   6.40 -0.67
    ## WRITWORK    2 3300   2.40  1.02   2.33    2.39  0.97   0.06   5.80   5.74  0.32
    ## READHOME    3 3300   2.75  0.79   2.69    2.70  0.60  -0.30   7.43   7.73  1.54
    ## READWORK    4 3300   2.52  0.90   2.43    2.46  0.73  -0.56   7.02   7.58  1.39
    ## NUMHOME     5 3300   2.48  0.80   2.50    2.50  0.70  -0.51   6.17   6.68  0.06
    ## NUMWORK     6 3300   2.34  1.03   2.29    2.32  1.01  -0.09   6.05   6.14  0.40
    ## ICTHOME     7 3300   2.40  0.85   2.42    2.39  0.79  -0.79   7.71   8.50  0.38
    ## ICTWORK     8 3300   2.20  1.11   2.06    2.12  1.21   0.01   5.46   5.45  0.61
    ## PVNUM1      9 3300 278.39 48.33 280.80  279.62 47.85  65.13 432.07 366.94 -0.27
    ## PVNUM2     10 3300 278.71 47.92 280.56  279.76 47.63  66.85 438.64 371.78 -0.22
    ## PVNUM3     11 3300 279.24 47.76 281.71  280.23 46.86  89.42 425.68 336.26 -0.22
    ## PVNUM4     12 3300 277.94 48.26 280.87  279.39 47.39 101.46 429.04 327.58 -0.29
    ## PVNUM5     13 3300 278.57 48.65 280.48  279.61 48.30  82.52 439.68 357.16 -0.22
    ## PVNUM6     14 3300 278.10 48.81 280.67  279.28 47.59  98.06 436.09 338.03 -0.25
    ## PVNUM7     15 3300 277.51 47.54 278.99  278.57 46.14  44.33 458.28 413.95 -0.24
    ## PVNUM8     16 3300 278.09 47.38 279.38  279.11 47.33   0.00 424.23 424.23 -0.26
    ## PVNUM9     17 3300 279.23 48.35 281.56  280.55 47.21  20.76 431.29 410.54 -0.30
    ## PVNUM10    18 3300 277.53 47.66 279.48  278.78 47.92  90.74 445.03 354.29 -0.25
    ##          kurtosis   se
    ## WRITHOME     2.17 0.01
    ## WRITWORK     0.26 0.02
    ## READHOME     7.20 0.01
    ## READWORK     5.06 0.02
    ## NUMHOME      2.48 0.01
    ## NUMWORK      0.75 0.02
    ## ICTHOME      2.13 0.01
    ## ICTWORK      0.00 0.02
    ## PVNUM1       0.18 0.84
    ## PVNUM2       0.09 0.83
    ## PVNUM3       0.09 0.83
    ## PVNUM4       0.10 0.84
    ## PVNUM5       0.10 0.85
    ## PVNUM6       0.17 0.85
    ## PVNUM7       0.25 0.83
    ## PVNUM8       0.30 0.82
    ## PVNUM9       0.29 0.84
    ## PVNUM10      0.10 0.83

#### K-means Clustering

USing the kmeans() function from base R:
[K-means](https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/kmeans)

##### Elbow Method for Optimal k

From the previous analysis in Python, the elbow method suggested a 3
clusters solutions.

This chart displays the use of elbow method to determine optimal k in R.

``` r
wss <- numeric(10)
for (k in 1:10)
  wss[k] <- sum(kmeans(data, centers = k, nstart = 30, iter.max = 100)$withinss)

# Optimal k plot
plot(1:10, wss, type="b", main = "Optimal K", xlab = "Number of Clusters", ylab = "Within Sum of Squares")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-16-1.png)<!-- -->

##### Determine if there is/are any valid clusters

``` r
library(factoextra)
```

    ## Loading required package: ggplot2

    ## 
    ## Attaching package: 'ggplot2'

    ## The following objects are masked from 'package:psych':
    ## 
    ##     %+%, alpha

    ## Welcome! Want to learn more? See two factoextra-related books at https://goo.gl/ve3WBa

Using the Hopkins statistics with get\_clut\_tendency () function in the
factoextra package. Note: This part of the process takes a while to
calculate the hopkins statistics.

``` r
# It is recommended by Daniels (2018) to first evaluate if clusters exist in the data with the Hopkins Test. 
Hopkins <-get_clust_tendency(data, n=nrow(data)-1, graph = TRUE)
Hopkins$hopkins_stat
```

    ## [1] 0.8825858

The Hopkins statistics value (threshold 0.5) indicated there are valid
clusters in the dataset.

``` r
# Generate a random dataset from the bkg_num for comparison 
random_df <- apply(data, 2, 
                function(x){runif(length(x), min(x), (max(x)))})
random_df <- as.data.frame(random_df)
```

The Hopkins statistics is also applied to the random set of the date for
comparison.

``` r
random <- get_clust_tendency(random_df, n = nrow(random_df)-1,
                          graph = FALSE)
random$hopkins_stat
```

    ## [1] 0.4996791

The result of 0.50 is consider expected for random data.

``` r
# An alternative with the clustertend packages. 
library(clustertend)
```

There is another package - clustertend which implement the 1-H values
here. Therefore, be aware of how to interpret this value with the
hopkins() function, in which the threshold is still 0.5, but looking for
values below that by 1-H.

``` r
set.seed(123)
hopkins(data, n = nrow(data)-1)
```

    ## $H
    ## [1] 0.1174142

For this, the value is expected to be below 0.5 for indication of valid
clusters in the dataset.

``` r
hopkins(random_df, n = nrow(data)-1)
```

    ## $H
    ## [1] 0.5003945

The random dataset also generated the expected value close to 0.5. We
can now proceed to clustering. For further information of using Hopkins
statistics or other metrics, see Adolfsson, et al.(2019).

##### Determining Optimal k with other methods/metrics

Using the nbClust package, it allows us to explore the optimal value of
k by a variety or index or metrics.

``` r
library(NbClust)
res<-NbClust(data, diss = NULL, distance = "euclidean", max.nc = 10, 
            method = "kmeans", index = "all")
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-25-1.png)<!-- -->

    ## *** : The Hubert index is a graphical method of determining the number of clusters.
    ##                 In the plot of Hubert index, we seek a significant knee that corresponds to a 
    ##                 significant increase of the value of the measure i.e the significant peak in Hubert
    ##                 index second differences plot. 
    ## 

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-25-2.png)<!-- -->

    ## *** : The D index is a graphical method of determining the number of clusters. 
    ##                 In the plot of D index, we seek a significant knee (the significant peak in Dindex
    ##                 second differences plot) that corresponds to a significant increase of the value of
    ##                 the measure. 
    ##  
    ## ******************************************************************* 
    ## * Among all indices:                                                
    ## * 7 proposed 2 as the best number of clusters 
    ## * 11 proposed 3 as the best number of clusters 
    ## * 1 proposed 6 as the best number of clusters 
    ## * 1 proposed 8 as the best number of clusters 
    ## * 3 proposed 10 as the best number of clusters 
    ## 
    ##                    ***** Conclusion *****                            
    ##  
    ## * According to the majority rule, the best number of clusters is  3 
    ##  
    ##  
    ## *******************************************************************

``` r
res$All.index
```

    ##        KL       CH  Hartigan      CCC    Scott      Marriot       TrCovW
    ## 2  3.4084 4168.435 1787.3793 171.5696 16745.28 5.606710e+88 1.565473e+13
    ## 3  2.5458 4106.221  885.9749  43.0444 19007.19 6.356430e+88 4.480297e+12
    ## 4  1.8350 3767.283  564.0502  27.5821 20611.58 6.949387e+88 2.098251e+12
    ## 5  1.7736 3448.954  361.0754  26.3551 21978.84 7.175104e+88 1.275252e+12
    ## 6  1.8896 3132.784  219.2752  28.3068 23129.90 7.289645e+88 9.466854e+11
    ## 7  1.7069 2820.129  146.8706  30.1184 23985.25 7.656547e+88 8.082027e+11
    ## 8  1.2801 2545.273  121.2717  31.5784 24733.21 7.972251e+88 7.388928e+11
    ## 9  1.0752 2323.610  112.6942  33.2340 25423.12 8.186377e+88 6.939513e+11
    ## 10 2.1618 2148.027   69.5361  35.3467 26191.55 8.007142e+88 6.607975e+11
    ##      TraceW Friedman    Rubin Cindex     DB Silhouette   Duda  Pseudot2   Beale
    ## 2  33679412 2309.332  78.1740 0.1735 0.8872     0.4423 0.8222  388.5162  2.7006
    ## 3  21841970 2330.576 120.5410 0.1593 0.9191     0.3725 1.3043 -466.3433 -2.9113
    ## 4  17215732 2349.171 152.9330 0.1628 1.0002     0.3174 1.2312 -253.6656 -2.3423
    ## 5  14700082 2370.103 179.1046 0.1577 1.1184     0.2706 1.6071 -532.2826 -4.7130
    ## 6  13248296 2393.658 198.7314 0.1580 1.2328     0.2363 1.4052 -265.3049 -3.5968
    ## 7  12421426 2415.883 211.9606 0.1554 1.4174     0.1979 1.6730 -432.8594 -5.0169
    ## 8  11891074 2441.435 221.4142 0.1547 1.5720     0.1683 1.7802 -447.4839 -5.4645
    ## 9  11468590 2467.901 229.5707 0.1619 1.6189     0.1575 1.2357  -94.5918 -2.3768
    ## 10 11088872 2506.486 237.4320 0.1752 1.7036     0.1465 1.6862 -319.0555 -5.0715
    ##    Ratkowsky     Ball Ptbiserial   Frey McClain   Dunn Hubert SDindex  Dindex
    ## 2     0.3263 16839706     0.5354 0.5550  0.5059 0.0323      0  0.0335 91.0184
    ## 3     0.3007  7280657     0.5611 0.9716  0.7888 0.0282      0  0.0310 75.2136
    ## 4     0.2701  4303933     0.5281 1.1078  1.0605 0.0408      0  0.0333 67.7761
    ## 5     0.2494  2940016     0.4904 1.1455  1.3542 0.0417      0  0.0381 63.1588
    ## 6     0.2317  2208049     0.4586 1.7592  1.6379 0.0443      0  0.0423 60.0191
    ## 7     0.2155  1774489     0.4199 1.6659  2.0338 0.0359      0  0.0520 58.0629
    ## 8     0.2031  1486384     0.3934 0.7791  2.3725 0.0460      0  0.0587 56.8048
    ## 9     0.1920  1274288     0.3869 1.3239  2.4757 0.0354      0  0.0610 56.0017
    ## 10    0.1826  1108887     0.3728 2.1716  2.7003 0.0508      0  0.0649 55.1181
    ##      SDbw
    ## 2  1.9699
    ## 3  1.0068
    ## 4  0.2496
    ## 5  0.2168
    ## 6  0.1969
    ## 7  0.1844
    ## 8  0.1757
    ## 9  0.1738
    ## 10 0.1699

``` r
res$Best.nc
```

    ##                     KL       CH Hartigan      CCC   Scott      Marriot
    ## Number_clusters 2.0000    2.000   3.0000   2.0000    3.00 6.000000e+00
    ## Value_Index     3.4084 4168.435 901.4043 171.5696 2261.91 2.523606e+87
    ##                       TrCovW  TraceW Friedman   Rubin Cindex     DB Silhouette
    ## Number_clusters 3.000000e+00       3  10.0000  3.0000 8.0000 2.0000     2.0000
    ## Value_Index     1.117444e+13 7211204  38.5844 -9.9751 0.1547 0.8872     0.4423
    ##                   Duda  PseudoT2   Beale Ratkowsky    Ball PtBiserial Frey
    ## Number_clusters 3.0000    3.0000  3.0000    2.0000       3     3.0000    1
    ## Value_Index     1.3043 -466.3433 -2.9113    0.3263 9559049     0.5611   NA
    ##                 McClain    Dunn Hubert SDindex Dindex    SDbw
    ## Number_clusters  2.0000 10.0000      0   3.000      0 10.0000
    ## Value_Index      0.5059  0.0508      0   0.031      0  0.1699

``` r
res$All.CriticalValues
```

    ##    CritValue_Duda CritValue_PseudoT2 Fvalue_Beale
    ## 2          0.9404           113.8173        1e-04
    ## 3          0.9331           143.3807        1e+00
    ## 4          0.9278           105.1661        1e+00
    ## 5          0.9285           108.4396        1e+00
    ## 6          0.9249            74.6486        1e+00
    ## 7          0.9232            89.5092        1e+00
    ## 8          0.9203            88.4136        1e+00
    ## 9          0.9157            45.6874        1e+00
    ## 10         0.9147            73.1545        1e+00

##### Assigning participants to the 3 cluster solution

``` r
groups <- kmeans(data, centers = 3, iter.max = 200)
```

``` r
print(str(groups))
```

    ## List of 9
    ##  $ cluster     : Named int [1:3300] 2 2 1 3 3 1 1 3 2 3 ...
    ##   ..- attr(*, "names")= chr [1:3300] "3" "4" "5" "8" ...
    ##  $ centers     : num [1:3, 1:18] 2.4 2.55 2.37 2.4 2.42 ...
    ##   ..- attr(*, "dimnames")=List of 2
    ##   .. ..$ : chr [1:3] "1" "2" "3"
    ##   .. ..$ : chr [1:18] "WRITHOME" "WRITWORK" "READHOME" "READWORK" ...
    ##  $ totss       : num 76247766
    ##  $ withinss    : num [1:3] 7686830 7698956 6456217
    ##  $ tot.withinss: num 21842003
    ##  $ betweenss   : num 54405762
    ##  $ size        : int [1:3] 1501 1087 712
    ##  $ iter        : int 2
    ##  $ ifault      : int 0
    ##  - attr(*, "class")= chr "kmeans"
    ## NULL

``` r
groups$centers
```

    ##   WRITHOME WRITWORK READHOME READWORK  NUMHOME  NUMWORK  ICTHOME  ICTWORK
    ## 1 2.404063 2.400465 2.705618 2.490846 2.403043 2.265859 2.337762 2.112506
    ## 2 2.550517 2.422546 2.804155 2.578905 2.685901 2.543870 2.645114 2.487268
    ## 3 2.373770 2.380248 2.764839 2.511140 2.321421 2.203106 2.173304 1.936856
    ##     PVNUM1   PVNUM2   PVNUM3   PVNUM4   PVNUM5   PVNUM6   PVNUM7   PVNUM8
    ## 1 273.6075 273.6609 274.7819 273.9361 273.7170 273.5577 272.7748 272.8964
    ## 2 326.8892 326.9654 326.8048 325.7793 327.6097 327.0958 325.0352 325.8308
    ## 3 214.4073 215.6605 216.0103 213.3528 213.9421 212.8860 214.9400 216.1696
    ##     PVNUM9  PVNUM10
    ## 1 275.0797 273.0050
    ## 2 327.2414 325.2731
    ## 3 214.6720 214.1648

At this point, we are uncertain if the solution is good unless we
evaluate it. The silhouette coefficient metric was used in the Python
version and is also used in this R version.

#### Model Evaluation

Silhouette Coefficient

``` r
library(cluster)
# Calculate the silhouette coefficients
result <- silhouette(groups$cluster, dist(data))
# Plot the result of Silhouette coefficients
plot(result, border = NA, main = "Silhouette Plot of Cluster Groups", col = 4)
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-28-1.png)<!-- -->

``` r
#Check the best number of clusters in the dataset
distance <- dist(data)  # Compute the Distance Matrix between rows of the data
avgS <- c()
for (k in 2:10) {
  cl <- kmeans(data, centers = k, nstart = 30, iter.max = 200)
  sil <- silhouette(cl$cluster, distance)
  avgS <-c(avgS, mean(sil[,3]))
}
```

``` r
data.frame(Clusters=2:10, sil_coefficients = avgS)
```

    ##   Clusters sil_coefficients
    ## 1        2        0.4423354
    ## 2        3        0.3724789
    ## 3        4        0.3143544
    ## 4        5        0.2711117
    ## 5        6        0.2362918
    ## 6        7        0.1981865
    ## 7        8        0.1798565
    ## 8        9        0.1583294
    ## 9       10        0.1473994

##### Visualizing the overall cluster result by 2 dimensions

``` r
fviz_cluster(groups, data = data)
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-31-1.png)<!-- -->

##### K-medoids Method

Using the k-medoids methods to partition the data and compare to the
k-mean clusters

``` r
# pam() function use sums of dissimilarities as search criterion
pc <- pam(data, k =3)
# create a table to compare the k-medoids result, with the k-means result
(cm <- table(pc$clustering, groups$cluster))
```

    ##    
    ##        1    2    3
    ##   1    0  967    0
    ##   2 1308  120    0
    ##   3  193    0  712

``` r
# groups$cluster is the k-mean result display as the horizontal header
# pc$clustering is the k-medoids result display as the vertical header

# Calculate the error rate between the k-medoids method and the k-mean method

# Total error rate
(1-sum(diag(cm)/sum(cm)))*100 
```

    ## [1] 74.78788

In this comparison, cluster 3 is stable with the proper assignment of
the membership between the two methods. Cluster 1 and 2 have a portion
of the participants assigned to a different cluster based on this two
methods.

``` r
# Retrieve the sillouette coefficients of the k-medoids method of 3 clusters
pc$silinfo$clus.avg.widths
```

    ## [1] 0.3609847 0.3794210 0.3318846

#### Visualization of the cluster memberships from k-means method

Data Preparation for Viz

``` r
# create a column in dataframe format of cluster membership
membership <- data.frame(groups$cluster)
# append the column of membership back to the dataset 
data$cluster <- membership$groups.cluster
```

Create cluster membership specific dataframe

``` r
clu_1 <- data[ which(data$cluster == "1"),]
clu_2 <- data[ which(data$cluster == "2"),]
clu_3 <- data[ which(data$cluster == "3"),]

# Check the kmean cluster assignment under groups and verified that the subset of data is correctly assigned
```

#### Scatter Plots

``` r
# alpha determines the opacity of the color, 

# theme centered the title 

library(ggplot2)

ggplot(data=data, aes(x=PVNUM1, y=ICTHOME, color = factor(cluster))) + 
  geom_point(alpha = 0.3) + 
  geom_point(data=data, aes(x=PVNUM1, y=ICTHOME), color = "#293352", size = 1, alpha = 0.2)+
  ggtitle("Scatter plot of ICTHOME index and PVNUM1 score") +
  theme(plot.title = element_text(hjust = 0.5))
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-36-1.png)<!-- -->

``` r
# stat_ellipse() compute normal data and add a range circle
ggplot(data=data, aes(x=PVNUM1, y=ICTWORK, color = factor(cluster))) + 
  geom_point(alpha = 0.2) + stat_ellipse() +
  geom_point(data=data, aes(x=PVNUM1, y=ICTWORK),color = "#293352", size = 1, alpha = 0.2)+
  ggtitle("Scatter plot of ICTWORK index and PVNUM1") +
  theme(plot.title = element_text(hjust = 0.5))
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-37-1.png)<!-- -->

``` r
ggplot(data=data, aes(x=PVNUM2, y=WRITHOME, color = factor(cluster))) + 
  geom_point(alpha = 0.2) + stat_ellipse() +
  geom_point(data=data, aes(x=PVNUM2, y=WRITHOME),color = "#293352", size = 1, alpha =0.2)+
  ggtitle("Scatter plot of WRITHOME Index and PVNUM2 score")+
  theme(plot.title = element_text(hjust = 0.5))
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-38-1.png)<!-- -->

``` r
ggplot(data=data, aes(x=PVNUM2, y=WRITWORK, color = factor(cluster))) + 
  geom_point(alpha = 0.2) + stat_ellipse() +
  geom_point(data=data, aes(x=PVNUM2, y=WRITWORK),color = "#293352", size = 1, alpha =0.2)+
  ggtitle("Scatter plot of WRITWORK Index and PVNUM2 score")+
  theme(plot.title = element_text(hjust = 0.5))
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-39-1.png)<!-- -->

``` r
ggplot(data=data, aes(x=PVNUM3, y=NUMHOME, color = factor(cluster))) + 
  geom_point(alpha = 0.2) + stat_ellipse() +
  geom_point(data=data, aes(x=PVNUM3, y=NUMHOME),color = "#293352", size = 1, alpha =0.2)+
  ggtitle("Scatter plot of NUMHOME Index and PVNUM3 score")+
  theme(plot.title = element_text(hjust = 0.5))
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-40-1.png)<!-- -->

``` r
ggplot(data=data, aes(x=PVNUM3, y=NUMWORK, color = factor(cluster))) + 
  geom_point(alpha = 0.2) + stat_ellipse() +
  geom_point(data=data, aes(x=PVNUM3, y=NUMWORK),color = "#293352", size = 1, alpha =0.2)+
  ggtitle("Scatter plot of WRITWORK Index and PVNUM2 score")+
  theme(plot.title = element_text(hjust = 0.5))
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-41-1.png)<!-- -->

The scatter plots showed the groups have areas of overlapping as well as
outliners in each cluster. Further work is needed to explore the
dimensions and noise in the dataset.

#### 3D Scatter Plot

In the Python version, we have 3D plots to examine how the clusters
positioned. This is an example of a 3D plot in R.

``` r
library(scatterplot3d)
```

``` r
colors <- c("#999999", "#E69F00", "#56B4E9")
colors <- colors[as.numeric(data$cluster)]
scatterplot3d(x = data$PVNUM1, y = data$ICTHOME, z = data$ICTWORK,
              main = "3D Scatter Plot",
              xlab = "PVNUM1",
              ylab = "ICTHOME",
              zlab = "ICTWORK",
              pch = 16, color = colors,
              grid = TRUE)
```

![](Analysis-in-R_files/figure-gfm/unnamed-chunk-43-1.png)<!-- -->

#### References:

  - Adolfsson, A., Ackerman, M., & Brownstein, N. C. (2019). To cluster,
    or not to cluster: An analysis of clusterability methods. Pattern
    Recognition, 88, 13-26.
    <https://doi.org/10.1016/j.patcog.2018.10.026>
  - Charrad, M. (2015). NbClust v3.0 in R Documentation.
    <https://www.rdocumentation.org/packages/NbClust/versions/3.0>
  - Daniels, L.(2018). Cluster Analysis Lecture.
    <https://lukedaniels1.github.io/Bio381_2018/Daniels_Cluster_Analysis_Lecture.html>
  - Everitt, B.S. Landau, S., & Leese, M. (2001). Cluster Analysis (4th
    ed.). Oxford University Press Inc.
  - Kassambara, A. & Mundt, F. (2017). facroextra 1.0.5 Documentation.
    <https://rpkgs.datanovia.com/factoextra/index.html>
  - Maechler, M. (2019). cluster v 2.1.0 in R Documentation.
    <https://www.rdocumentation.org/packages/cluster>
  - Torgo. L. (2017). Data mining with R:Learning with case studies. CRC
    Press
