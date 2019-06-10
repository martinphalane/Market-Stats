{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Martin\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello Martin\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('Data/WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(9134, 24)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method NDFrame.head of      Customer       State  Customer Lifetime Value Response  Coverage  \\\n",
       "0     BU79786  Washington              2763.519279       No     Basic   \n",
       "1     QZ44356     Arizona              6979.535903       No  Extended   \n",
       "2     AI49188      Nevada             12887.431650       No   Premium   \n",
       "3     WW63253  California              7645.861827       No     Basic   \n",
       "4     HB64268  Washington              2813.692575       No     Basic   \n",
       "5     OC83172      Oregon              8256.297800      Yes     Basic   \n",
       "6     XZ87318      Oregon              5380.898636      Yes     Basic   \n",
       "7     CF85061     Arizona              7216.100311       No   Premium   \n",
       "8     DY87989      Oregon             24127.504020      Yes     Basic   \n",
       "9     BQ94931      Oregon              7388.178085       No  Extended   \n",
       "10    SX51350  California              4738.992022       No     Basic   \n",
       "11    VQ65197  California              8197.197078       No     Basic   \n",
       "12    DP39365  California              8798.797003       No   Premium   \n",
       "13    SJ95423     Arizona              8819.018934      Yes     Basic   \n",
       "14    IL66569  California              5384.431665       No     Basic   \n",
       "15    BW63560      Oregon              7463.139377       No     Basic   \n",
       "16    FV94802      Nevada              2566.867823       No     Basic   \n",
       "17    OE15005  California              3945.241604       No     Basic   \n",
       "18    WC83389      Oregon              5710.333115       No     Basic   \n",
       "19    FL50705  California              8162.617053       No   Premium   \n",
       "20    ZK25313      Oregon              2872.051273       No     Basic   \n",
       "21    SV62436  Washington              3041.791561       No  Extended   \n",
       "22    YH23384     Arizona             24127.504020      Yes     Basic   \n",
       "23    TZ98966      Nevada              2450.190996       No     Basic   \n",
       "24    HM55802  California              2392.107890       No     Basic   \n",
       "25    FS42516      Oregon              5802.065978       No     Basic   \n",
       "26    US89481  California              3946.372085       No   Premium   \n",
       "27    HO30839  Washington              5346.916576       No  Extended   \n",
       "28    GE62437     Arizona             12902.560140       No   Premium   \n",
       "29    EJ77678      Oregon              3235.360468       No  Extended   \n",
       "...       ...         ...                      ...      ...       ...   \n",
       "9104  LM97847  California              2615.139220       No     Basic   \n",
       "9105  IK96366  California              5551.398167       No  Extended   \n",
       "9106  SJ86522  California              6827.044423       No     Basic   \n",
       "9107  UU42868  California              5619.689084      Yes   Premium   \n",
       "9108  GX11087  California              3907.028747       No     Basic   \n",
       "9109  JR41742  California              3622.872124       No     Basic   \n",
       "9110  RA89822  California             34611.378960      Yes     Basic   \n",
       "9111  IJ25462  California              2845.520933       No     Basic   \n",
       "9112  ZP86347  California              5500.577411       No  Extended   \n",
       "9113  HO82823  California              3358.532935       No  Extended   \n",
       "9114  EA54906  California              7501.661322       No  Extended   \n",
       "9115  BC64697  California             11663.985720       No   Premium   \n",
       "9116  VV68726  California              5133.397765       No     Basic   \n",
       "9117  QR91631  California              8732.090534       No     Basic   \n",
       "9118  OT56964  California              9424.256842       No     Basic   \n",
       "9119  YX35990  California              5479.555081      Yes     Basic   \n",
       "9120  RN61682  California              2114.738469       No     Basic   \n",
       "9121  BB10681  California              4140.648654       No  Extended   \n",
       "9122  FH43628  California             25464.820590      Yes  Extended   \n",
       "9123  WZ45103  California              5678.050167      Yes  Extended   \n",
       "9124  CB59349  California             16261.585500       No  Extended   \n",
       "9125  RX91025  California             19872.262000       No   Premium   \n",
       "9126  AC13887  California              4628.995325       No     Basic   \n",
       "9127  TF56202  California              5032.165498       No     Basic   \n",
       "9128  YM19146  California              4100.398533       No   Premium   \n",
       "9129  LA72316  California             23405.987980       No     Basic   \n",
       "9130  PK87824  California              3096.511217      Yes  Extended   \n",
       "9131  TD14365  California              8163.890428       No  Extended   \n",
       "9132  UP19263  California              7524.442436       No  Extended   \n",
       "9133  Y167826  California              2611.836866       No  Extended   \n",
       "\n",
       "                 Education Effective To Date EmploymentStatus Gender  Income  \\\n",
       "0                 Bachelor           2/24/11         Employed      F   56274   \n",
       "1                 Bachelor           1/31/11       Unemployed      F       0   \n",
       "2                 Bachelor           2/19/11         Employed      F   48767   \n",
       "3                 Bachelor           1/20/11       Unemployed      M       0   \n",
       "4                 Bachelor            2/3/11         Employed      M   43836   \n",
       "5                 Bachelor           1/25/11         Employed      F   62902   \n",
       "6                  College           2/24/11         Employed      F   55350   \n",
       "7                   Master           1/18/11       Unemployed      M       0   \n",
       "8                 Bachelor           1/26/11    Medical Leave      M   14072   \n",
       "9                  College           2/17/11         Employed      F   28812   \n",
       "10                 College           2/21/11       Unemployed      M       0   \n",
       "11                 College            1/6/11       Unemployed      F       0   \n",
       "12                  Master            2/6/11         Employed      M   77026   \n",
       "13    High School or Below           1/10/11         Employed      M   99845   \n",
       "14                 College           1/18/11         Employed      M   83689   \n",
       "15                Bachelor           1/17/11         Employed      F   24599   \n",
       "16    High School or Below            2/6/11    Medical Leave      M   25049   \n",
       "17                 College            1/5/11    Medical Leave      M   28855   \n",
       "18                 College           2/27/11         Employed      M   51148   \n",
       "19    High School or Below           1/14/11         Employed      F   66140   \n",
       "20    High School or Below           2/19/11         Employed      M   57749   \n",
       "21                Bachelor           1/21/11         Disabled      F   13789   \n",
       "22                Bachelor           1/26/11    Medical Leave      M   14072   \n",
       "23                Bachelor           2/24/11       Unemployed      F       0   \n",
       "24                Bachelor            2/5/11         Disabled      F   17870   \n",
       "25                 College           1/29/11         Employed      M   97541   \n",
       "26                Bachelor           2/28/11       Unemployed      F       0   \n",
       "27                  Master           2/12/11         Disabled      F   10511   \n",
       "28                 College            2/2/11         Employed      F   86584   \n",
       "29                  Master            2/7/11         Employed      F   75690   \n",
       "...                    ...               ...              ...    ...     ...   \n",
       "9104               College            1/9/11         Employed      M   57023   \n",
       "9105               College           2/22/11         Employed      M   36918   \n",
       "9106  High School or Below           1/12/11       Unemployed      M       0   \n",
       "9107  High School or Below           1/26/11       Unemployed      M       0   \n",
       "9108  High School or Below           1/28/11       Unemployed      F       0   \n",
       "9109               College           1/25/11       Unemployed      M       0   \n",
       "9110  High School or Below           1/14/11         Employed      F   20090   \n",
       "9111              Bachelor            2/7/11         Employed      M   86631   \n",
       "9112               College           2/12/11         Employed      F   44019   \n",
       "9113              Bachelor            1/6/11         Employed      F   59367   \n",
       "9114  High School or Below           2/23/11         Employed      F   38874   \n",
       "9115               College           2/17/11       Unemployed      F       0   \n",
       "9116  High School or Below           1/26/11         Disabled      F   28647   \n",
       "9117  High School or Below           1/20/11         Employed      F   51205   \n",
       "9118                Master           2/10/11         Employed      M   46897   \n",
       "9119                Master           1/13/11         Employed      M   56005   \n",
       "9120              Bachelor           2/19/11       Unemployed      F       0   \n",
       "9121               College           1/17/11       Unemployed      F       0   \n",
       "9122               College            2/1/11          Retired      F   13663   \n",
       "9123              Bachelor           1/19/11       Unemployed      F       0   \n",
       "9124                Master           1/20/11         Employed      M   60646   \n",
       "9125  High School or Below           1/31/11       Unemployed      M       0   \n",
       "9126              Bachelor            1/9/11       Unemployed      M       0   \n",
       "9127               College           2/12/11         Employed      M   66367   \n",
       "9128               College            1/6/11         Employed      F   47761   \n",
       "9129              Bachelor           2/10/11         Employed      M   71941   \n",
       "9130               College           2/12/11         Employed      F   21604   \n",
       "9131              Bachelor            2/6/11       Unemployed      M       0   \n",
       "9132               College            2/3/11         Employed      M   21941   \n",
       "9133               College           2/14/11       Unemployed      M       0   \n",
       "\n",
       "      ... Months Since Policy Inception Number of Open Complaints  \\\n",
       "0     ...                             5                         0   \n",
       "1     ...                            42                         0   \n",
       "2     ...                            38                         0   \n",
       "3     ...                            65                         0   \n",
       "4     ...                            44                         0   \n",
       "5     ...                            94                         0   \n",
       "6     ...                            13                         0   \n",
       "7     ...                            68                         0   \n",
       "8     ...                             3                         0   \n",
       "9     ...                             7                         0   \n",
       "10    ...                             5                         0   \n",
       "11    ...                            87                         0   \n",
       "12    ...                            82                         2   \n",
       "13    ...                            25                         1   \n",
       "14    ...                            10                         2   \n",
       "15    ...                            50                         1   \n",
       "16    ...                             7                         0   \n",
       "17    ...                            59                         0   \n",
       "18    ...                             1                         0   \n",
       "19    ...                            21                         0   \n",
       "20    ...                            21                         0   \n",
       "21    ...                            49                         0   \n",
       "22    ...                             3                         0   \n",
       "23    ...                            44                         3   \n",
       "24    ...                            91                         0   \n",
       "25    ...                             1                         0   \n",
       "26    ...                            47                         0   \n",
       "27    ...                            64                         0   \n",
       "28    ...                            54                         2   \n",
       "29    ...                            44                         1   \n",
       "...   ...                           ...                       ...   \n",
       "9104  ...                            59                         0   \n",
       "9105  ...                            77                         3   \n",
       "9106  ...                            26                         0   \n",
       "9107  ...                             5                         0   \n",
       "9108  ...                             8                         0   \n",
       "9109  ...                            52                         0   \n",
       "9110  ...                            59                         0   \n",
       "9111  ...                            44                         1   \n",
       "9112  ...                            60                         0   \n",
       "9113  ...                            48                         0   \n",
       "9114  ...                            86                         0   \n",
       "9115  ...                            34                         0   \n",
       "9116  ...                            59                         0   \n",
       "9117  ...                            52                         0   \n",
       "9118  ...                            11                         0   \n",
       "9119  ...                            30                         1   \n",
       "9120  ...                            69                         5   \n",
       "9121  ...                            35                         2   \n",
       "9122  ...                            66                         0   \n",
       "9123  ...                            44                         0   \n",
       "9124  ...                            42                         0   \n",
       "9125  ...                            35                         0   \n",
       "9126  ...                            21                         0   \n",
       "9127  ...                            48                         0   \n",
       "9128  ...                            58                         0   \n",
       "9129  ...                            89                         0   \n",
       "9130  ...                            28                         0   \n",
       "9131  ...                            37                         3   \n",
       "9132  ...                             3                         0   \n",
       "9133  ...                            90                         0   \n",
       "\n",
       "      Number of Policies     Policy Type        Policy  Renew Offer Type  \\\n",
       "0                      1  Corporate Auto  Corporate L3            Offer1   \n",
       "1                      8   Personal Auto   Personal L3            Offer3   \n",
       "2                      2   Personal Auto   Personal L3            Offer1   \n",
       "3                      7  Corporate Auto  Corporate L2            Offer1   \n",
       "4                      1   Personal Auto   Personal L1            Offer1   \n",
       "5                      2   Personal Auto   Personal L3            Offer2   \n",
       "6                      9  Corporate Auto  Corporate L3            Offer1   \n",
       "7                      4  Corporate Auto  Corporate L3            Offer1   \n",
       "8                      2  Corporate Auto  Corporate L3            Offer1   \n",
       "9                      8    Special Auto    Special L2            Offer2   \n",
       "10                     3   Personal Auto   Personal L3            Offer1   \n",
       "11                     3   Personal Auto   Personal L3            Offer2   \n",
       "12                     3  Corporate Auto  Corporate L1            Offer2   \n",
       "13                     8  Corporate Auto  Corporate L3            Offer2   \n",
       "14                     8  Corporate Auto  Corporate L3            Offer4   \n",
       "15                     2  Corporate Auto  Corporate L2            Offer2   \n",
       "16                     1   Personal Auto   Personal L3            Offer2   \n",
       "17                     1   Personal Auto   Personal L2            Offer3   \n",
       "18                     7   Personal Auto   Personal L2            Offer2   \n",
       "19                     3  Corporate Auto  Corporate L2            Offer1   \n",
       "20                     1   Personal Auto   Personal L2            Offer1   \n",
       "21                     1   Personal Auto   Personal L3            Offer4   \n",
       "22                     2   Personal Auto   Personal L3            Offer1   \n",
       "23                     1  Corporate Auto  Corporate L3            Offer1   \n",
       "24                     1  Corporate Auto  Corporate L2            Offer2   \n",
       "25                     3   Personal Auto   Personal L3            Offer2   \n",
       "26                     1   Personal Auto   Personal L3            Offer1   \n",
       "27                     1  Corporate Auto  Corporate L1            Offer1   \n",
       "28                     2   Personal Auto   Personal L3            Offer1   \n",
       "29                     1   Personal Auto   Personal L3            Offer2   \n",
       "...                  ...             ...           ...               ...   \n",
       "9104                   1   Personal Auto   Personal L2            Offer2   \n",
       "9105                   3   Personal Auto   Personal L1            Offer1   \n",
       "9106                   9  Corporate Auto  Corporate L3            Offer2   \n",
       "9107                   1  Corporate Auto  Corporate L2            Offer2   \n",
       "9108                   1   Personal Auto   Personal L2            Offer1   \n",
       "9109                   1  Corporate Auto  Corporate L3            Offer1   \n",
       "9110                   2   Personal Auto   Personal L2            Offer2   \n",
       "9111                   1   Personal Auto   Personal L2            Offer3   \n",
       "9112                   1   Personal Auto   Personal L3            Offer3   \n",
       "9113                   1   Personal Auto   Personal L3            Offer2   \n",
       "9114                   3  Corporate Auto  Corporate L1            Offer2   \n",
       "9115                   2   Personal Auto   Personal L3            Offer3   \n",
       "9116                   3   Personal Auto   Personal L2            Offer1   \n",
       "9117                   2   Personal Auto   Personal L1            Offer2   \n",
       "9118                   3  Corporate Auto  Corporate L3            Offer1   \n",
       "9119                   3  Corporate Auto  Corporate L2            Offer1   \n",
       "9120                   1   Personal Auto   Personal L2            Offer3   \n",
       "9121                   1  Corporate Auto  Corporate L3            Offer1   \n",
       "9122                   2   Personal Auto   Personal L2            Offer1   \n",
       "9123                   3   Personal Auto   Personal L2            Offer2   \n",
       "9124                   2   Personal Auto   Personal L3            Offer2   \n",
       "9125                   2   Personal Auto   Personal L3            Offer1   \n",
       "9126                   4  Corporate Auto  Corporate L1            Offer1   \n",
       "9127                   3   Personal Auto   Personal L3            Offer2   \n",
       "9128                   1   Personal Auto   Personal L2            Offer1   \n",
       "9129                   2   Personal Auto   Personal L1            Offer2   \n",
       "9130                   1  Corporate Auto  Corporate L3            Offer1   \n",
       "9131                   2  Corporate Auto  Corporate L2            Offer1   \n",
       "9132                   3   Personal Auto   Personal L2            Offer3   \n",
       "9133                   1  Corporate Auto  Corporate L3            Offer4   \n",
       "\n",
       "      Sales Channel Total Claim Amount  Vehicle Class Vehicle Size  \n",
       "0             Agent         384.811147   Two-Door Car      Medsize  \n",
       "1             Agent        1131.464935  Four-Door Car      Medsize  \n",
       "2             Agent         566.472247   Two-Door Car      Medsize  \n",
       "3       Call Center         529.881344            SUV      Medsize  \n",
       "4             Agent         138.130879  Four-Door Car      Medsize  \n",
       "5               Web         159.383042   Two-Door Car      Medsize  \n",
       "6             Agent         321.600000  Four-Door Car      Medsize  \n",
       "7             Agent         363.029680  Four-Door Car      Medsize  \n",
       "8             Agent         511.200000  Four-Door Car      Medsize  \n",
       "9            Branch         425.527834  Four-Door Car      Medsize  \n",
       "10            Agent         482.400000  Four-Door Car        Small  \n",
       "11            Agent         528.000000            SUV      Medsize  \n",
       "12            Agent         472.029737  Four-Door Car      Medsize  \n",
       "13           Branch         528.000000            SUV      Medsize  \n",
       "14      Call Center         307.139132  Four-Door Car      Medsize  \n",
       "15           Branch          42.920271  Four-Door Car      Medsize  \n",
       "16      Call Center         454.245098   Two-Door Car      Medsize  \n",
       "17      Call Center         647.442031            SUV      Medsize  \n",
       "18           Branch         308.981664  Four-Door Car      Medsize  \n",
       "19      Call Center         484.800000  Four-Door Car        Small  \n",
       "20           Branch         355.200000   Two-Door Car      Medsize  \n",
       "21      Call Center         379.200000  Four-Door Car      Medsize  \n",
       "22            Agent         511.200000  Four-Door Car      Medsize  \n",
       "23           Branch         554.376763  Four-Door Car      Medsize  \n",
       "24           Branch         439.200000  Four-Door Car      Medsize  \n",
       "25      Call Center         389.185006  Four-Door Car        Large  \n",
       "26            Agent         799.200000  Four-Door Car        Small  \n",
       "27           Branch         516.237951            SUV      Medsize  \n",
       "28      Call Center         532.800000  Four-Door Car        Large  \n",
       "29           Branch         384.000000  Four-Door Car        Small  \n",
       "...             ...                ...            ...          ...  \n",
       "9104          Agent         250.652309  Four-Door Car      Medsize  \n",
       "9105         Branch         364.800000   Two-Door Car      Medsize  \n",
       "9106          Agent         956.689634            SUV      Medsize  \n",
       "9107            Web        1027.000029            SUV      Medsize  \n",
       "9108          Agent         666.042098            SUV      Medsize  \n",
       "9109         Branch        1254.177129            SUV      Medsize  \n",
       "9110          Agent         523.200000     Sports Car      Medsize  \n",
       "9111          Agent         400.832857  Four-Door Car        Small  \n",
       "9112          Agent         165.478147            SUV      Medsize  \n",
       "9113          Agent           6.880385  Four-Door Car      Medsize  \n",
       "9114         Branch         331.170924  Four-Door Car      Medsize  \n",
       "9115    Call Center         513.600000  Four-Door Car        Small  \n",
       "9116          Agent         331.200000  Four-Door Car        Small  \n",
       "9117         Branch         185.530076   Two-Door Car      Medsize  \n",
       "9118          Agent         322.575677            SUV      Medsize  \n",
       "9119         Branch         326.400000  Four-Door Car        Small  \n",
       "9120            Web         518.400000  Four-Door Car      Medsize  \n",
       "9121         Branch         590.400000            SUV      Medsize  \n",
       "9122         Branch         465.600000  Four-Door Car        Small  \n",
       "9123          Agent         364.800000  Four-Door Car        Small  \n",
       "9124          Agent         643.200000            SUV      Medsize  \n",
       "9125          Agent        1950.725547            SUV        Small  \n",
       "9126         Branch         482.400000   Two-Door Car      Medsize  \n",
       "9127    Call Center         307.200000   Two-Door Car        Small  \n",
       "9128         Branch         541.282007  Four-Door Car        Large  \n",
       "9129            Web         198.234764  Four-Door Car      Medsize  \n",
       "9130         Branch         379.200000  Four-Door Car      Medsize  \n",
       "9131         Branch         790.784983  Four-Door Car      Medsize  \n",
       "9132         Branch         691.200000  Four-Door Car        Large  \n",
       "9133    Call Center         369.600000   Two-Door Car      Medsize  \n",
       "\n",
       "[9134 rows x 24 columns]>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Customer', 'State', 'Customer Lifetime Value', 'Response', 'Coverage',\n",
       "       'Education', 'Effective To Date', 'EmploymentStatus', 'Gender',\n",
       "       'Income', 'Location Code', 'Marital Status', 'Monthly Premium Auto',\n",
       "       'Months Since Last Claim', 'Months Since Policy Inception',\n",
       "       'Number of Open Complaints', 'Number of Policies', 'Policy Type',\n",
       "       'Policy', 'Renew Offer Type', 'Sales Channel', 'Total Claim Amount',\n",
       "       'Vehicle Class', 'Vehicle Size'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Response\n",
       "No     7826\n",
       "Yes    1308\n",
       "Name: Customer, dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Response').count()['Customer']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#visualisation od the data in a graph\n",
    "ax = df.groupby('Response').count()['Customer'].plot(\n",
    "    kind='bar',\n",
    "    color='red',\n",
    "    grid=True,\n",
    "    figsize=(10, 5),\n",
    "    title='Customer Interacton '\n",
    ")\n",
    "ax.set_xlabel('Interaction')\n",
    "ax.set_ylabel('Count')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Response\n",
       "No     0.856799\n",
       "Yes    0.143201\n",
       "Name: Customer, dtype: float64"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculat and finding % of interaction and non interaction with the market \n",
    "df.groupby('Response').count()['Customer']/df.shape[0]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Renew Offer Type\n",
       "Offer1    0.158316\n",
       "Offer2    0.233766\n",
       "Offer3    0.020950\n",
       "Offer4         NaN\n",
       "Name: Customer, dtype: float64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Finding inetratinf rates per renewals offer \n",
    "by_offer_type_df = df.loc[\n",
    "    df['Response']=='Yes', #counting on engaged clients \n",
    "].groupby([\n",
    "    'Renew Offer Type'# intereacted clients grouped by renewals offer\n",
    "    ]).count()['Customer'] / df.groupby('Renew Offer Type').count()['Customer']\n",
    "by_offer_type_df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 504x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Presenting data in a bar plot\n",
    "ax = (by_offer_type_df*100.0).plot(\n",
    "kind='bar',\n",
    "figsize=(7, 7),\n",
    "color='purple',\n",
    "grid=True\n",
    ")\n",
    "ax.set_ylabel(' Interaction With Client Rate in Percentage %')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
