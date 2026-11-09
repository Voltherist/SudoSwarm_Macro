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
_C1d = "d28c879d0874c41e02198e47647f42d0a7e7b164b606f7058a62f13129447114"

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
 "x4=Z52=g5RcUv%V1bc%%!F`V=>;>=GeL<J_>*1vb{Fi@ffpbcn6w-Jw-3gI)IB;Alazr2+K`;3y3",
 "j_r&FIpQ&N5I?bymzpTUl!MZ}gQ{7i0;rUkR}U|I=3w~Sx$a6G{~{eIPh(OgEy2oykMC_Q0>?-bP",
 "klz$)51o({1niX>2Bnw=vM&n+gp7ZH;+QTCZw^n#MjzES{t`JLFuE&gNZtHDVH9RKET{1tP6?*E*",
 "zTu|%fPKgN?#o_j^L8n%SMxP*b3^N9>yL6=P3VSH>r}qgc^8a^e5RDz!3kUZK+t4NuwRlq=q^*Yb",
 "y0I8uZuWRA9?z9l0nSyZNg`i@qcEej@HLJ&}8$$)%4YeuRzl!=r|?VnV#pYObf<+Aaz{q%Yzidwp",
 "5|8xUN&}SM`N)_!LS;wTjZewF*Pqe!l-{g1)D7*@XRV{|{~QeFA{H+Ljo;f3p=FVb$`%yedkg=Rs",
 ";D<=hAw++qnW;KM>)?c${K?U<xB<zCE}_T(OcIUhOL8z}|!gc(DgW0{;kThz!TZQJbuXBh4am#*S",
 "7a4o@LO}a>Gjjn0b@J63C$_bt^AIbCVe@K~s?;A19VPK%&tdY3w+-mvLK3Nz<-*M2Jx1V<TJ_nvF",
 "A{`HT*c?0)hfxB1GRgk&3S#3&<D8X=IbdHNsb4xuC7yY|&|dllJ>qbvTLHjhaFWbgF#-82u6Rl43",
 "%f0CX3{{^jk|3yHH+1w8o6CPOc(?|4iq2hMf9@__OJt<Mm(^D@<c3CveI}r^RiL8B}rMHD*m4L)#",
 "+Q;u{@V_s#;efnvk$F?=e^`tr4K(kNOO?<~u?&E@@sDS=@Y)#|m1drPyCdT*2<!payFKa+Qlj1vS",
 "vPZhB&(i_Ymeg_n|WS^#1wQ{MY+8{0*>0raxs49HyeD#Taz6bR$VMe*B}$zt<2<2xYGK4uOL5Db4",
 "b4Agm+6$t9l%?Uu3+j)Q$MCt54X65x$L{D>0LPmE9#V87tbv8O@9iR!OA1Ll?jVd$6MpO67dD9*c",
 "s7=%tL(m$gGGu(5<!VU$WXt2ztT^}v-h(?+2z|+;3%PO-eo0Ykg{2~5c3#R$7NzY&66w`0BNDwv8",
 "0P%TV{1u4)d~^l1q$~sMs1v-HlNS=rDb$_z9oJE7IVIQfHwyH)X&*VTpTeo3tcRR-*ti$cntClPG",
 "UcktF&hS{L}IBIsj)*Be6-bHD;L`?vi@z0@K9}@i10qK`B+}oN0hgCU{~ID&5EuX&|b|+F!BArGJ",
 "wqFa}dvEO?Vxz`6r8)dcpXW_y%*az@SvNxpcvSq!o+5;j}|K;HSs#B}n7(85-^_dm1}W<qweZXEo",
 "ajOQ?iY0^0UQ*pn=|Cm%J)Zq-rp41V%j9`V+f`^P7ch>rv;V}k9MZ1bO0U9iF?im~~UJ{%7pS|>H",
 "**P(K;Q8b!uRt}3?Fhs~oyiJ@!7&u`X+#o@*RGJE8<gk$f~J!D8kyiQ`w$9b6S<3#JM>%y138D3^",
 "P&$5JT<g91zHXWDU)6c7tZykn84>$YuCc{*%qJ4%6TVpg(N<pfg^1=L&_Ft3K3WPnUQsrPrA8Y0C",
 "_%{rHPqW0HBx62P?C*yY{sye6ZRkxXSN%J<(s1=sUO;&@0C<fcKj{jC(U()Jh@l5yO<;i8Voa66k",
 "_30ZM%jZ&lc?o~nuGa*)vgUGBF~dQaW}{Q|M_w$9AY6#cK*GA;w>{Br^!ZWf-`<-z@3)&%L9(|@Q",
 "cDb<?_?9<&TccRQ#nOFOhfRKI9-&er{@9Y15fC-QP!UVAKo;vBnBvwkK^Me4@cf23Ltw3yZtKzOP",
 "8tEsQXZl#NFCr3QCSm~V9=`{<1RRQ`>BG-aPuicke?}ztXnLGC5t$^W`Sz{+?T+<;?X?8QhQXtB#",
 "X@JRix)uwlv7pDWPj(mx(lnut5JS1KgJH#mBgOBO#HzKs@5M^dp$LS9!=OEh|Nq2b?~S@T5&HTop",
 "BC)|I-IQARMRB6vT~ARd&b^b(l;Y4--TI*$)H6veAAE_`_J=Id%d#xC&rkHTK%Ojc4c@F!o^SCO`",
 "nI@f(|eAw%v`P;3{l^aKnQOZQOg)xeg#W$Uet9YNkZEnPHVZE%UWE|lMFxd|2<^}H!<y{>k$^C!0",
 "YKDUf;UMU<+LUdW7OR|gMV~NeEF(o@1Psp7Btrh<GcKh#f{oKvZ49k0a3@<N#U7!{n(FVuKBfdR!",
 "kXW4Z8MfqrRW_m9oiar5sM^aoE`$;hdc|oaaHJnvh|M6ef>E*}KG>p(Zvd`}Z&bBcHWm+5yx-=6H",
 "$_0KXma4fN}UhtY&ZeArs2n^y1C_A9cfoI(vyNXid3=BBxUZb6O?=N*U8}+Fa-2rqj}k+ak)O}0{",
 "KXiD+%`073<5J+GRo)o0p$J5v7(IA{{w0vp+{9s=Dwr5&$4~52Ij!SrKigBgx<F{);zkBYrAUH2I",
 "EE;?+G04jdci3kH)3!hrk8=OG@H5giy%Ue5XBOe^lqX?^$8JBJI9=l1vAR}&`mdfv6001Heqsc-3",
 "_!PQcx1@*#lNv{MoC~;nXwf*W}ayxwfc!bX4RN)F6#{tL0sJYU(RTcr7x`KBLB(rSvDSWh@fYQDk",
 "=I954%W)=RLxbh*rt0lEPL&;P#to&;XHH0jfM$%kz|k(FlN1zHo-MAfVS7xzO4WeqM)k9e=6qMft",
 "7R2pSw;kbwhoddAfDZnYv9*YBLo7Xl#{qZAjWv3%(Gi%AVelEa>{ss8`GncsEUM(yfNK~tcwP6Uy",
 "K5S7+3wS*bi3txWZNto2KU>HH<3z;tBzEPm-K)4bJ07{DQTl+R%T~Y>Fl)XH^P{xWZ+bu*#wC#bq",
 "pUwvXX?j=SHp<Ba$^O$V3CW1lJaZnPv2ub^e;m;j6tX_g-mDuy@LD%%OWgq8<K<YW+g%Mhhh;u-(",
 "(Oi1n@RWglcWp1V<oYY7V?mxOuFkmN$=(Qd{a?Mh!DtMHSc@1LIw#d=k8sYDiCaT*iM5VRPV<X-%",
 "3H}@CA%~4tAtzNIep|O8L$1IN1~zEW7*CFBe=Q>ei&jjDD2|`6?Lb0~k}RWYVki3E^(ML>e8!j+!",
 "jzh<>m{n+x)J)S431>VkuJsoquB;<#_6Ys@rcQF_twSIj3GMTcu0)1aQkfQ8iq2r@;H%E->0efO_",
 "D`5%kb6=Hv|ghecCOO`iugTp0J@DrAHQ$L+7S@!!F_>4W`uOQo)oSv;*(o8KvYnVhuwjh-Yc7pU`",
 "%ro=+Ocf97u->6xiu_Y-;Q>EQTh0H;Wjtg-XEx+g8`hsPIuT-jJoyT!g1sCB5bnDhnUDek}XpY+3",
 "E^r+`Otgx)iI6k23H(kA=1;0lfsBc%eDQBhoLvQKuN2SV@O=@BFm*H&&{6egEc%}Lzm(nxr$#*{)",
 "SAtY?(Z21b|Hr-xg*rTu+qwhK@g0PKa(NKb@%FHjt7?Q%ZE*Mk)4>DyX_qMPlQU<eyi!{yMngT%n",
 "<b$rD4dEVp#sMlfkN*|L&dMTO59_O9H1xZ!-gy%^sp4bv1@vTP6HQx7|%c`ZYdaC>Xj>QJaCTUOP",
 "WOf-23W#D)xOhu_sIDSoN|=5DRYksLECLjK2Sp-<iel5NeYn|LGwzL<mqH3T`sSGPt8?n{mkq%_0",
 "a_t`mk}aU3jTow9uidptv$k7!3I4|m*dgn0uP%rnc+Z>GjPi(m3n?XRfLna$O%`%Z|-y3AyMxSHY",
 "2fL}tx_mT0B3npV#)~Ja^bT-}A=Tk1`V*IT#3T7~ti9!zziO7Gb_dVv}b`<=5<+wg}ER{vV!81@m",
 "WUCJySm@nu|9%N0TMw!k=lT!M?5X5xAfSK0?FFp&L^=K@OL`?c1o4EWRG#s>y&9M_wN?9Hud$Z)k",
 "Tf`uY|}BJUJ@+mwJ5+3$zw0*Xw#Lzm2xXv3>O?8=V-1-GAB&aCBObVw=3d$u#^@Y(247mvodf5+0",
 "U+RunhlE%&@FgN7=+u&aCfW6i*hs(c|yD?E}wg4>ruO-%lO>Uws#KI^2pU)I@v<`#PQQZxTK<Iwy",
 "a6z7H9;oUW_x!-;*|c}tIwNA8WYd>L?lT=a;BUJ2Auk@4m9w)ao*#6eoM75iclA+<~pD8?(iOl$i",
 "5RRA{{nHzZHlCjWBlfi6=Un;Mofxr>pzTzdq`;4J30{le>)6@?-j93%bg*Xe-d7899BJN!@tG}^=",
 "GfUgjckx&F3hC2xN113jIMc135-GC0H@_GLE$YcLiD#X-0*sF~ZhhX)?v+<dCfdFk`L(ZO)E$SD`",
 "<g9%k}apR*3^#Llz)y{NINM#_?vj`$M81i)*B6z$fwYnKn|<KwJ=A~1YI0n^_M1`0uLh|Qw<0^xS",
 "L;CrIBp+b$YD@qt2BFA|F-sKA_A`&k;}(hYs*3I^MUMOnEgcn8wU`KO$1)Q)r0`YY18@8|}D*k;M",
 "D|)e4)I0nM{CH#Y!mEn)p+xOL!Rhyen^*kvedGg*kl%5XCNwVQYKcmF+s>E4|VOsO8(4MQB<X}-l",
 "Lm|}Hr%&olY1zU@mfIkFHAH|d5!xCq6KXw<kzA4jQY>UX(irewbbqERe7=N4=jXmph#JGvdewSd8",
 "2eb$bHkC>Dlx$it+q&K)H(=@<1uVtfO~RrT50E)l!aFaE0O`rOJaV;o+}Oc6Id4@pHO*Scq!dxj#",
 "N1r%DjVA"
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
