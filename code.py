A=matrix([[1, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2],
[0, 1, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1],
[0, 0, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1],
[0, 0, 0, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1],
[0, 0, 0, 0, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1],
[0, 0, 0, 0, 0, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2],
[0, 0, 0, 0, 0, 0, 1, 3, 1, 1, 2, 3, 1, 1, 2, 3],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 3, 1, 1, 2, 3],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 3, 1, 1, 2],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 1, 2, 3, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])




#matrix has to be broken into n*1 matrices
#here the dimension of A matrix is 16 * 16 so the text has to be broken into 16*1 matrices
#create a dictionary mapping letters to their numerical value
#take 16 characters from input text and multiply their numeric value by A inverse
#convert the numeric result using dictionary..hence we get the decrypted value

encrypt="Ic7NWOhO[2%/rFOiJB!ms5LnNm.d3S( F6,7-0=P}K};2]?cTL\"^i~-P@q2A(Hrx~i7FR!?1'h3VsQGi6O)yoIgy-FR:gU5r?s-i8E5kzz)?~A) RFoe3%,M[(1)v@/ ;Xx6EUrY^d@=9X r}4ZG1057eLQ;l*- hD%:Bv\n[ulVEp&+a3Z)vB8G7}Dp7^0jt$vyn^[RgnJ^v@PXh%fVGJPyUCfO:sCFdj5K)\n^Z1mVQ@DH( 4'-luynPu:mX Cu\" Ld! 6lGp7=vuR2nqR@+;,}6+bmPRkperSl3C:Dd!+DEZ2\np659S2$Fgyb{wqb..F.ijq8.2u]=b5FPkpEWE%ZVlx-\"Bv00plv?:-.R\nH!M]ue:,la$t38:&+ N)v@/ Y^S$n{THPhu(P6kocDiS/9B1Ih1P:0bthDKAz,Y?by-d\n4\nk.E8\"G+F\"Ap\"Q,(- fkaJ)a/%boz6R1wuJ9]l*o&4:$;s8S9sK}.m-6B?E{B.8   ^'4A8nk=;PL=:B% O3h87NYp(Vx9(QCe8A%:-x*.3z,r[QDhGPteR3\"X/=L]f$@dSAQ(~?j:OEVEQS\"hQY$z8GM,CcmZRN) h?cL80v'mN6*m{{\nko3V4uttLGPAKS\"i%6O^78J!UbS?VLH }:vc9C\"Yf]C{!QOg t,r/f)pZ=L-7]{\n!y/]BAby!]7ZCu:,{sxitSGb[5~k]5ateH}dgI)04Ypf5heo$tcTv9g[]XU!'C$ a]m4v00-Nk{w7   &7!=u3NlRY6J(U\nlApq2CQ'1zF9H.C/ T0.q1G5ilY8MFO% y,%/@YS!'Si26nttu]aV.2y,}46PNN) yqndn!mJ%qa1'PGiJHVLkNt^JpbPYLH I2'lP3^i@!rF:K?cuFDshhnu}V;8~ZGi3q0$E*\"~AMh3?RCe),{meah;!L J: ate,/ Z)x[G?K&LattW}{cinLdR[LB^LThi:N%h\"&2JtWAj@*eICB~JHo{(%A~~OWhcDYC=%BGaoM*qJ%enw]x=h7p%y1;[DHe6UteHI@,bAt\n$ZOi3VfA$;xEy^8HsC!d6^;4Z0Xz@WkFFQZi}CE+o^0d16bL}l..~eF~dlvBiOaP/R4oO@%/GG4tu\"s4;5btcpX$S^2+]65IL\"\"i'z'bDw0.;6L^h@!d{}iG?[C6mpVG'F2nGe&=b@4y/QY)oA{a6F}dhx,:GUoek$~ E-]./*5-fmgOMMMe)jI;TGT6mTiRnOYojMI-[1{\nym@u5EHi:hh8)!:F{Dx9$J!c7%E~+ pCfSF^*d;y5S(.K%3eiKY$sA[ scD~iCG;73aO:-^aHS2T6a] Le&]e{}a$x&sd*hz'rhVE3kry^TEL\n1v=JdR?RCe(9:k1??deekZ3y%,n@J'x=Wx\nslU\"KE 1:aES5M4}\n({iQ\npgl^q)13pU/uk;C+amc$-:kho$fx5CW9olO/mES&E]}?s/Hc~JqYIw9=7N=M*!GMf/pWEff}8+s+i7   B,~sqiWU$}.9wg%aMo=4D;\n{d'-xAb8s}85DJXA2qLoe0ettu!w96y&cu5 I?PAdXExnJkeoxQ},5EHiR::5Us)1 He4\"U1in%Q*/&g*{!L@;L4~DwXFqWxx.\"X!$5bp@F]vGe1[R/5EZMG \"rWM'^s)!+jTftztF,jYit'1Rlg.BMQeyq]lPDvVAY~!nV6rz)C,xn{t?/)/.CHe0vvdm5r,Ny$oCCFdFcp oA-9&tZK:LKh@G*x(.5PCurhQs-.1~{}'vWGCPqZ]kpybWnd4%Hw]3Q~]MIe'\"J:~YIGDVo/w*AdfYDFbIWu/R\n(l*- H't2ea5jv&:R[U) /czaMJTT,/ZP%qclra6Yu/k.k'~og'%,+:ucmWU1nuVL'G/ 4px4Sd@9r+5L,9at'Ck\"*GK6v0ik7[V\"}(k GoAbO!g2H32n-iUWc/CH;fL*r2) Xr4SzS=S;R&]4%%ehqN(=wNgy;L$s6eu8!,dq6^LUtzkdh!dD!jH@BrE,t:aC~R~LA;4bNc,?59U9gfnP.EyYL,l8=}oxW8o{2)?uN@P'OjUpIWno2O!F^&1f{+isCFd:Rsa@9O8^U/[3@!diS+ +a1tH$la1AIi-[0(U]Xv@iiM(32nuLvjejx2lI TFO% ,7j 6\n.).X:g=,\nlS*O/:7hL ~[u&U\"iSRwm7DT.%nwdhZG *dlUNf4:?^BvqQ2n V9G'g1%8Mj 27am{HVKBXGUn$[X?48s1C\"Arddmq\nQ;l*- Q;A['okEJj'g8wsu!-eSh*]2r0ik7[V\"D\nG!eJ:)eR:t9jjrJT){8L5xiXW!,?HrBN=Ix$AuLLnd~J+a+5s\nE*6;bE)/BR%ei7*t^3X$:+lPWXOeweS)8I6!K0L+1?+a35YFZwQgm:)zrmpr=5i4Ud\n/$\"Q[}C* V?SDFu\"qCAF=?aNo$+%-S-'Ks^(+BJMdNb=a?p/%Ij4Wx5atJuSDmd\nkI$9JxQWnKH+o*=;/4IbrS67atxeI=z'Jf2h\nJMMe=Sr\"+ZTVHQ-KrN0oPBR{ }JJ?saJVRE /9bK{:1a'HnI%($ ;t(}$gD3}1 TGq9w{@h5Fk+AYFtjCZOid)N~yyx=\"WwhMK&aBfA[f]$QoYwj7   ;cw3*O.R.~pbM[S~\n(+uG^y^d[,r[QDhlT&=VB&&arh7]L+a)X'u)l[)Qc!'=C$ AdY)&;Sz~78Br*[ EJQ]vA1m^~U%vQ\"nDQjS~%9w\naiM?C*cN^/bg\"Iw7]kVRhrs()@lqw7+2tw31YXh/lcLU\"8glKu3Wgfn}+6PrY;7^.F^CPXhbf?q7va~8X{,3S* WTVCI7l8Ll abd/ Or\nDj,SmqQCw{INe]Z]mDftWMP'p3R% {]+heyo/7X{t7ADh/jKA@(XrzJdR?RCe,+G.vRRR+l!1};Ce4&hIiODs@^(:Ctuae%QGIpLtzo2]qF&dQK]AErn$wvs-bL7 L\nb28j:8tTD$YswMs?v^BZd Z ~:$PXhtW'sb[Z$f,,31YXhOvy I7+M\ni]i\nBGi6cxnCM*U^*v6{NBg~*;6jR)szIVL'G/ !7Q}IUp&rjt\nJY\nlh*C-?A\nl!/I('($ T[{,ca4+1PpfV?}cRO]n@&mI@;C/t*CeSFD~gg{\n=I+wdYeu)W:t  0bC1r5'*CeStwdg 8}(5kZFO% qL2P\nKp}@7iM=aat$w;s2?mBAHO/+SXj4K};E\"=O+VcWL2jr\nU;n8exKa2te4M\"ok(uk*d[JB.B{y%^a8UrcNDBR?exm~D]a@W[]a'r;{4]zpQ2n\"Xv4(OAhKA5O!IJfMLaP)d3wEq~v3EQl%fy5P14w}N3J!YOir,oY0RF;se)}uR2n2Q'nBvLz0Nqb1gjr\nsgVgp}}}BF]^PXh&I6G/5(7R;Z/tU2n.@oZ6-V.!%C?^8jrZ84CSd(n6[$'F6Yo[rJ(D9d(L)H*I7jpS]bW@\"(0^& \n1UQeNc)lve,4O-pf%G/ v}^uj 0g^nd!q(?c+{O/bZU.SmYOzY rl'P*uVWq!j^'9OYoMyG=c2$[^-vwx\"  L?+wOmx)@d5TzG*f'f[8$q'B[Xk7MLfu .dxQp\"sM0pfh3ReYIaZ2U3=WDSIDPXhW;[]EsdB18bOJKJcBJ0SdL7t%4.bKN@ Umwmy}*\nh0ik7[V\"hIM:tI[E iF^cIWnlKB]$.^*Mgr45^AeA;\n%Ws/s3LgQ@EqEVda0v-M18)3O/[V\"7;}x%is?F,(}{\"dpS9C:QhZ?U\"t4]L&dDB-o)83-\nFzoShjt!R NF9/EOcjK,5atRZc~\"3xCyVD:KL\"-R+z750s+*~A=sQ2n\"e$mC5Q=dbN[*J+aXcG&]Ma&H&E[qQ2nHlR]JOZ*z3p 3WFa$ahR~&3:LgKAhW8s$\"bR&vp]W'0SDapuu\nWJ cm[YZiZ\nettP~C;+B)FNk(qN[R~8;[md9}~]CU&pICfez2Ff?LN?(=i?&\"-hI1GC=\"sGF8VVfkryC^qgq)aPKcTHQOgn8)yKqX^LnaUJQFdrL4)VupU:gUK;TUlX3F^5Iz:1;j ]RIij@x\n5j^CCCA=wDIeuy~pODe'vc[q1z},=(V!x)+2[L2PWXOeTKwd*8\"@ 3{,3S* e*TIGvO+3F-xRUDd!{z53ADbl4bKFO% d~vg$Ylo+uPormprQYN+]px)*@D@O6ko5dA~bT]5O2g6aQE $}b2H\nU0*F=h@M!dG3vkkpRmJBJ^BKOey$T?htQ\"Lf'i8wsu\"tgZhdKhN G&r5pyHy@o\n+:CB)arVVGehYAp]@yxR8wX]H(eNjv2T24A48R(N\"{\n2)'6 &(F8Oo Q38nLvlaFbh&}9*+o&Ae1cLBb65rRk/JG78nRjy2KgCoNT1('LKhK^VDJMqGF3XBJbprYkk4o40$b&Apja8l}BA}1=Y--m6TyC!dlhzk8i^OEfgWUXQe~yRB,+]F3!A Cbbt%YY)MvCEYESIDPXhiTq\"=?dHn@0SWTCaDGjS7^28/$WIISKe9V@huF+EhlSItXdts:laA^N.}6fTFO% ^guf4B1r'}L$;bowkXLrDj9mJj\nN,\ndt , NOA**k]&rNmjt0e~kO~wF4NN%-\n^iDr2(U4a=@ajS?RCef~m\"bbJ1M\"zh PA lM4CwgviSbya4usuQ'pfIV\"+\nPV&n?~an;I($iG8~/LBONReX5VL 8o{Ti%={MIe 7%/ZE9y'^F'4&@d0/L]bVR8~/LBONRehPDu,vDpxN5LHEXh$  JA+yy\n5X)v@/ \n.h\neSOl'*^qpQ2n5kO'@gs?F,(}{\"dpyFV(gx[{J%Q!5!!dCy;:ER}H;\nQ];$bt%}NzO o-@2C@gYbt99;naH~LpW};gPWna@&vq@/G-?X)v@/ D3$yKoXoBzUVF 5oQ/tju,@F(3bSJb8oZHGvjsv*W$2USdst=;bQurtqwHE}OKG \"piR\n,DDS)U(~I6~$d8L@]Px*ciZ4efoP0a1xAImuri4yyUWCV,dNNApDWaL;A] y3jZZl&\"dz?j7&CfpWk8\nJG,hRXFH0Wip$PFLKW}V?E'=D! 07e03(Kd}O@+AhjwbSo3&$MjqT/x8U s@\",7u{/Sl\ndSC6ot4VeSU/S;1R3&q?~a+cxjoARt;FBv.LUizMEy-7UwPR3&q?~avX\"Om j%Ly(:aUbtKKSAA8B=hmbOSs~.Ob~:&%**\n,&+(I) 0f:h\nP)4rn]x=(* +H%/GaH0:De\nXAB~A4HI]rsG5]L:dB@d1p=mh/Glx8pai^r G[7Gq*g{S6j20   *wJ[9RUWo?U^nG*fO+@mYdsHqyX(l4hv5/+dih6~MORHb3;Ikh}oS/Nu+\"9TQdao]fe5p)hA;[WM3JTmrzgP0Kn)]sqZ00cD.gT&1:=Nm2x4}gqsArZK~i%aMGY^{CHeWe7Up77pD}h8EH@ Z~YNKpER!.R)v@/ 0OCtyd7(^;R%dQWne)G&iBy-ZgH*e$*e?yjNOB'S=@VHFF( lpo0R%vUdUeUF otPfe'M.\n3*zG?wK4~3vi1miuuJS3R8jyt%f^5-LJ1&JqZ{ at)D6YPZRm:gxe0   C.{ihj@UD4xnf^r oDMCT(~QgJOAE,Jt%+=cfwMMV7+c]M{\nJS1)'aHwE&O)@C* hbYJrHp(aL'h*gjwvqF@:59zY?Z)a]+a~cSH}1f[]RlZF 2nh7K*q,?U.\"&l]PGiyNbP~IZ+eD5KCX oNtj9$J$jJZ;fY]+arT4R1D3vvfcNY\"QeVDF=/z* q!C,e0cDUd7M\"XN=I-qW9SG 3@N(%Pprmeyjkv'iTWVLuJ8tzrq\nFQZigPF]$gGRm('31YXh4+Y%ok\n,M/9P+epyBJ6GxV%3v,lPPMReV^yoM?lJ]9RHwX\npw8/wo\nRh,32UZ6koG\n\"Q5qWxPO0D'\"\"-&p()f\nC.6rE%p1jwml*r0v=HsX,Pm[qIx]=m:E8dP4WKff~MTm$-LV3'k:5o[IMe!F!qpUOW:ylZ\"(/t- \"&Q,IKXjwiwGMfneN{\nodv;I6K?RCer\nbV/lTrdv4R:3ry:d-x,g{?^Th8\n\nPe;t\"Lm(Uzc\"=qd~{avZXH3Y!0%ma}v@/ QzVK?:UTX$\nD[J~ant;91~K1,j0N'ajwPVTG6}RTY(A=(I) xXu2Evb{Fs&=qQ2n{HN;r\"2&X{'cdTG V4WM9+uJ'0O)Qiat 1 0vZaEA/lb*N;I3IjTx;hp?2M/KFE A([zH&6$Pb9\"p;\"YYKoePsL6PQXIOt@,T@6Kouu?O;0SDapuzXM)6cvYJhQBxR\no3zG&GtaE5F?\nPhmutNg7Emv(Tg?.'C$ QQ.hRfpt.]$z@PXh]+2q0Edtt\"Q[}C* }.B]@\"Kat{}o.GMfx==nv)^2:.\n*(CC~}{+c& 3+VoJ)i;},)=lZ\n\n?(GH5J{6it\"Ch8wG$m[Tp2* es6Ei;f?+%I!0ONs{,wMg20G%qcM1O0a8l!%G,z?Ne0&(z=Eb~3a-/$(g%?-aY?G$c2DSHH\nKGDVo/w*Ad.Ueg!]?i;a(t^gjwT1red@B3l?]gdmqs*tG/6W@0(W'=9$*e-R=~QdJ&*DF'u\"gs;IncYH%\ncUeUF otG=H}:a?FfeV*(CC~:Ze0!s.(?y$:sCFdej@rPm=8'k].qQ2n)D.9.uz&}p@qJs..kZ2:ngrMqEt6+J-\"/rwh-POiLtk6t%nH89-xkw5[0C\nKP1fojEQ!L17!R)=gml@dUB:]*hWu6'xV;G4o~t*+X)8Y\nrIX?jty UJ[!M?g\"I1;7Wsu\".^'t2OvYuw31YXhw(G=7XFDnX^,9^*fgSt7D*VXkb4RyH(eR~kU2$}GB[%PNEFaFw{soB^4*g;e9U) XhZPpFMoxP:oS!R?eK89A[XXb\"Y@$I% lS&=9aig)40(C)( UgS*g6wyq5ZAVRE MAxiD2ECI,z.raviD^gK5:;It5r9ZS\"h}+ND+wbo$oZK,5at^nA~/J9zk i*m{{\nPtG=l0pdr%Ucjv'ifi$-^6WfA@\n)wR\noG-)vi91d+2teQ38n,&8UC\nJn\n@CbTX].~-,;xVR,(b*YA~V!^I0K(Bn/,1iYFO% M;9\n$Uq'z}I/t0 rf*P+j+5^e/\nDkGSlSL1B]44k'+7/vFE vH3UY\nTbwaiM}S4nuGB!CqOoX@F~IPTm.qzl:OQi%EWMDH( z3+jL'$Y4\nE%~\n0o(6UW0F'VzL6X7rvtN3x6^to%ZnKAhW8s7sVG:y.@}6fTFO% GHBo8S[L/l$kMW;IB+a0BxRN0OG{CS{\njtCzL9:T!Drg9U) k6{wlOJZ88?o&9Yo&EC::RGU2hF=ZPqEv\"?rV@k@lWpfh3Re*IkZ?G!4@\"].EZUiXToYqZHz{S1E!QOgneg7ax] 0k7V+0btVs*{1cSm~m+rf*CeSJh4S]O4g]P*.+%afCL&-kh]-a+wn$L-A%K]]c9**-B+.0grByJ^za9'ROVCN1foA~*:'v?crH0AsA[ u4m81+f$8a$;9CC~sOG!'h,z&gG&zR2nBn)?h(Qq~m8\"x\"VnJQ:tQ3r:=Ci4NmjtXG$u=lCYAp*k7[V\"&'y53.H2s.6T~2\"njm;s.oRV[);'hW8soESE%@D5&&9Eh?+aOcD$z.BT9%XKFO% ,a@l+5{Y9C*zEX0i1Z, ,1\nvvNR$=C$ 5P?y3oN7LH8M?C*ca41k-q*E(RDyz3nu-:/y/ta+I1vJZett'7A~{CDkvG!t@FFayxGsM.&o?e$;8S9sXviYX.{D}{^IF\"8n&L1OWtY.S*ZC-U2n9OqrUD)240-w8wsu[~=gs!h,0npe{25rc(-d0sX:qeK{ ]+a~rI,Afj:].h7$3UlaWWY1wM3$&SIIHC YY3V Y&f*\nE%bKSm+-gP\"z1y2Hk6RQMeQ (} 6Yeub+j7   5[G{.evLiNIyhe6lXu&qXh$gYwWEw*Ce*ox9D:Jv]r&=v0jt :ABt2==K/9IP}v\"Trv1({}6+bmPRkpe,~j1y?!W^OR)IPXh(zUBx8&Y%7N(rZat*m3'xSemeI=\")b r=WH/*K%Xt~?:*bat;i-hXi3i.BL.a\"NeCWLBb65rRk/JG78n$-I(v]5^8im8Wnpr5XkU[+\n!cBj7FQOg2j~k)wgCjP5(OPJgLvnd?ee(UkZ)W6ko.T$-1Oaww\"Q[}C* ^FPA'L4z/U9SSWPebS%:aYfK^tE?[DHeOrD;RR31n?H+nC(ej6v2Evb{Fs&=qQ2nI6S$+u+')Sxy3w/.R\n-*@Lxz1s2P:0btFf*:6.q}!7aOOhls679JK\ngj[wO?3{[bE[H-r528fUi77t[yN.9YCJ4d.Dka0UCaCh;2)ZS-MCQCGM( ,l.cW$5}a5@fxVFe3vX%L9QQ+yUJEC* oxQB9'fDHwp2adWn.eh86;g{mYdO?Q2n{?F,xax?dS-3Qjms/qs0NyIoX@F~IPTm!?RDCRbbqgG!Z0ba.s3V,cnUTsZP,C(eOWH@e23t.48E[J~aL30(C 9D52r\n;(/ {q!m8+WvllM+O^8nHddS-XTt1H]oiWsu~Hb1\"nR,HLq3DecsQVi1V}?SM*uiFb4o'/g7]j7'Opw56\"Qe(G(+JF[J/?gK*D r}L(/T^8{i8&p;jzH?ED}G/^5zlpTASAd8z-u]N{8w?$nk)Ee]pD=nz2=c2+r }- 7DWvE:o&RH@v{hzHacJ^yUbx~~)?~A) .RTJ9S)R/7J%lNYoqvs\n3H7BCu&rHr+;diT^a0frJ7\nP?3 rP,ZPrMKh-/J)C6 o}1 X9RBc%W7F;A] TvcLSOL.Whr2RI) gG-x 3E vg[x.GMf9vcY+i*8XtYFksLTapj 1oT;a6=vogam*i.7SmM6{hLB&3 r;u@n4MTcp.b&r5pyVORH3YHT,1uvuR2n45XF\nb1nXWy%jRWnmOd34?q?s9]g=,\nlFnj NDh}l4!=oBAe=Oq3^Y5ep+iMU\"{\n:tb&3.*Pgiz1(aow6-6Fgr*)^AD=&:{h9m~'seWU$}.9wg%a+hgH&VE\n^uPF:B*c;7hYBGt,!s(.,Q\nlC!RH) Y~am&r4^*f2E@+AA69lTJii;JttRTILF86hp'a&YWlpL!=T3t}/NnY}c9sVLdR!?:yUz4P:0bt^.pY7^zPwE(smd8lEo\nQ=EyA{c*k7[V\"$gvivht[}'w\"S ttM:5Q[3vH=^[z{64ptAi4Lc!e5aaE}(Abtz Z'J:X,6qgZ\"\"i\n\nmcaT5,6fOEESDf[hzo:OVl?y%zkFOi!WQ-/6U1nuVL'G/ jftam?lBS=kmCPXhP[f3A5Ee]ZY]fOWhR+4Kx^/1=1F!q7py)o{,j}/38\"O^A1foODCy{,fevx9AO3jwe(AB\"q53[l0SwI%eG&\nM]&Ll~,{,p%^aK\nW$Ea6sWO}pNb rV{S%jw)r=!UF;OJg(?&jQm(aHZ7UAXMe3y~q7r*6X6u0!dfte2t6J0q^u$zpJ8 r}-6T'vj,I3G&dOYo-zgOSRfUnZ+v3$(eSc0Op?4xVv{h PA \"5PEdi:L9:{ha?~aS}hQibZh)wP%e(*f-F^w~zmy -;db;!.mJKL)$Q-B*WMDH( t@eUwyMqyh{Z/u~aZE{s*rkBiK^.(98s6?mZ99Ac;3j5R tt=V{,7-IRmL;nBbhuMQ\n?q+r(e^bMrS9s4xyjWog]%=*rcN0o9c$o(34&5c:q4UCai6M*8&]Tu6)?hgdo[Vj61W^)eC{pEkpyr,)vXXOCm];d}c9spB]s{k!A0:RCBSIeqa=('9SW.IE[}C* UW2BDy)kYer;qQUlT!/k-F\nt(N-xZ$U~6p)u7ytXc4\"*,V5ovhAz606]H\nlb00OewP5I^X:,;!~zy*(a$hYJhbDI&RD;]e,yM\"9us/*0SEjk/dowU+dM8+~K qnTX7or=F2P^!s)-?X)v@/ x3@s$LObdsyoKEFa$16FC&418z^wa7Zi6Qm8{zFkW;0R~B(b&~E%ENyB^ J-CS\"h3'3N%D.(:0K(m}- Rc@,st//D@I('($ Ba)=oS0f%iU~tC$ 4CpfJ[\nMK~3NTUCaYIzc(4b')Lt0+0Yo:LTEW%iyvJ2LNjptAxR!86!4E0&]iS6rS\n,9?G!4@\"].EZUi]\n+dz~eIeAAuiA&d?o!.9 o$*PN!$5bpD:{h0EJHtg)/w*AdF=r\"6!YqBYR}+LSiD8H*jQ4oA&XIH3dpD,rMoOOl{;)?~A) \";\"QyEvK@nPA[R2nBqU^1k4.W}nB/SXm\"eC,R7dx+P3I?RCe'Q2TM@888n{mL 5oIiWMfDyOE'M%u?~aHT&vK+t%7{?:Ca6rto.Ol]* oD^py*(aa~3V?3]Ca=DR?RCe5]S}3.BftqB{b@/ 8g%uI96nL9NDyWcsa@zbo4]5Iua}v@/ ]hJ&nU'U=T&]4%%e@5G!X+r$O))?~A) GeAvRpvKd?XI?RCeyDd3HL=VB0E!5/]bDIDxO&3&lc,id?~aZ6-e^E$^T6$;l*/ L$E?^g9lrL3VTS) wlSIq-g)l@$o9CC~~UPeFL+8LGaR*Y2n%6=4+x]bbTWD\"Rdy(\n^[4vEeMuF~,Q2nv0C/S3X9v*Gxj~{ b'aI2Ut!k-.,F9Yo[$w3oSPp!%eZ[4VnzJ0K*OA2G8j10mssw,~;F jl.,(t3BGi[yaJ6Sc~Ac;sn3G &QSD!m]XVov3?RCe\nzI-9RRdrZQ;l*- ,1bL-7fxWkI%s1( 1bz6~MC]Fdt5I6quNKka06f)ZOvJZett!HwhJeLq!=6X?RCe+s{eWsfsTh=h PA y;.48tNcjjmbo7;IZF^.(rn+O4Ex.J ~]c{wjqTsI@*jLYG z=zo%vR8!]7Hq(?cbqwhs'}WoKQ]m&/ 4qQG$6WkxVE.'C$ l&TIE~w%P;/[%PXhP/n6/HcGqr+ns%^aH4L{Or9^/nI,@FFaG&SI\n,M5l[O]iB*e=JF?P-vx1o-oqJ4~^c1KSMqN1xcMScqs=9W!)q$^Wqsdr%$ 31.7D*VXkb4RyH(eMWQ{x%CRg1v3-5atTU.m46O98M6*m{{\n^M&;0%b!fGtj1s,y/[2FjXXzRe8IN08m8!V@6YuNXBVL'D&dmsDEie*j{poXYO) 4BpZ P(7U,^u8wsuGjF'W,bu?cik7[V\")5WDE6kmqB6J?RCe~k HD-M4O *{)b rV!2M+\",\"HGw7&L&diPD}R1i/UWmW-5atP,yM}YNlA!0(rZatOqH*}2IiB?tiDo;,^KWM{Zn%CSmV'78snHf65UzGzr(u\"hjtbPjS:%DVH~9\"HEXhO!$..fxEf?\"B7]{\nRFi+dN{PA33HFF( y'7EZ=G9.B0OOhlsi7QB9{}7u/I(E55m0'cLH)lBfCqfab+aGKJ)N::8[aF~iXbt;3{k(*~L06*8b@/ RK(:R*a\nZ1RH~KIecWeN]&Rc+(1EwYYoWEFe$\"L'a6}I[LKhZB?: /sM8?7O?Q2nY1G^g?&S34A2HH@ {CI$MG{GU!YO^QOguA&nm-U+[C GtI9rAiO}R1x~]9TJ l1 fRk Z/]}U!\"L*X oqSM{&=.Vn.qZZettWPu7D*VXkb4RyH(e!dh8f-S{12XAHR\"iyHZ&5!){T,W6/E/ ^1h12-i8\"J&*n)( I{VGDqr*4ZaW1hxumirco/XyN-moKEFa((57FNglR(?:*batne/kUI[*;GJQCKFd+:XN,q7[eqM*}JFe&-QG,wGkzK8\"8por^I}vM2~T:zw4V^\n~l'1Lu4DC~imZFO% EBE:f%quP(9\nKODcr$H%EC=V3XDFl$@ -JM/tMvQ}zKA){B~z%de9~S9 J$n{JNe2Bm+cw+FgRdOuYat.(8nRK37fd TW=K-)m^:yxrFJBQ%-apv{X9OSX6+aXM*(CC~QlqzzVH1{:K@?GMfM)r ?-y[F6M-APXh!glbax7?na-sc%(eetB.4;a$$j^5]?Ulb!3HwA1i'&g1Cd rD@.i;}I\neJ(s{)( ~ThR=)\"@K1cIy7duMncLQ0W29TJii;Jtzh8HTD3}~ioYFO% 0vx\nXVu}B$!=s\n r/C;sP6.(- N)v@/ Jv&sS%eItg=mh*CeX$=uR=8:+YG;)1fo~6l7S+5/\nRC@;Q\nljGH&M?DYeI3VW rr'M XQ ,&w-SEz1(\nWs0tb!6qbS?VLH uC@ru,=5-:oe~R{\nC?Cwo\"%}5WhWxP2ow5]v2A]2uG5UKQ^ O(x32P}YQu'b^UCe\nnJyB$zRpWC~p2atrHeN;)R+ctL&l   Ndt8Ye0xU~\"&eejr:jpVD+w[Vh^;l*- IVnc6rcaQNX(l4hvjS~oI,FmyAZH~AUil3{hzGVJ6\"lb}D/ .TqgX&^k[r%-.GMf{kVCbfvB8?g6F1bpLSn bUrQ.5?l* at3Zsinji{60 QK8lsT7nom6Qk)@T(?HIe925X\n\ntJ0N^[zQ\nlm1~yg-Ii%S34!3kr9q3CN=ZV8Zzoa&BepTzd,z.Aj}^']C* IDa0L61jXXvh PA %n{,s)vEr^z8\"*CeJ{},U!5m7B9Aff[ W%naXO$SJgo0$ZOioZV)TdOm1{d\nyB*e4DJZNL/rm-!.s{8s%u+kkiBg3n)A[JSi4%f6\nXM4lk[sq$@ tA;sO6r!&pE?8KQlzNs5%Y-0/+bZ(6\"n3Nn7Rp~i].(x5IWnVLRSaea'SJ8\"bHu\"yJCb8?vLdE9\nW\nOew=[zXab[FCbKx5atRALB0y*\"hLT?sA[ )eD:OAp\nW2te4mrsM k5f1'6RxtYE(Oe}e$:'!(f;Ud\nEW8n^/\nCww\n:\";6LnOYo3 V)84@eQ8k6aQE XaJ[Hhn@6PrX.\nat19c~j!2yXDw ?1Yoe*(pj'mNt 2*HPXhSKcPA8kq-,P~t\ndt%QQFAw^1cr}m7^&dc*3H:rs%L$\n?@KGaXFH[n8d$FoL&fU0pb:[lq@ ~8voX3'^oJaI/RQAk3sr\"Go,yd)d\n&407Ju=dewWnc/ *zH%Ou%=c8;!.lUC;iPuY);L%~GMfQqN,4%%-O^j1:\"VnYM{t(T:U[2B}g?{a\"A3R%i'RvEr4*Y2nRR=mKw\n7TBu16UG h5jSH=sHom7UBQOgj/?jiwoH4oNDk0gvw.7FJY m/RtbM[S~nKE;,klyRz4WzB&dG1rgm7m-'/C-.GFd$k'4mG \"62[]Uz~U4dP8PJzI9?;(.CC~C~VWq}FfvBA[B5do:H$n;N(r)FA.-GMf;y?@SM;gKjt?k;{\n0qxL$PT*An6~/(/ i)^iY*NPNSk3NRHeMA1Fs4XWb$Q*uVarQewmom/YN6I:sCFdWUbP+gIv(xJ%jrqtD^w9,g@KP 4Vk8;I$E3M&VxOFEaQ:8fto*@o,j'CHNr\n.UYi{[4R{\"X:@]0FwE2o%7gP)LDLMrB!v-!.h(j w=Qov&\"&kPNkF=A=xkEfUzO?4'' mHK'ls)r0}%O0a8l$245o O:%kQ{OKG 4\n)t[ TdNM?sE?~awF?:\"OHwQwG&zR2n8yw@%Iy\"yPI:@C* CW5D;?XUi8%v \nMe11oe6c1=Q'P~b$(erzbL0vXqTQ$-2~}cEGz7tCWxcAzpXggs.b1)LD2886dOF otpStu24P:U:+d3S( NNlb u[O%5C@n?/ BjF-28m@0'1FmS9s)%lb\"@79^[3B Z?.tYv4c c=($YZwBFe!KbM'&m^yxk(m{{\nU@N?nN+F)\"7!!XNe1Z3U1uiPh1ufP}!dbJ5W8)6@rRN&Sjat~we5/QvNM(b\nJ$T~jxWHd1MgZQvTH0WiuWS'oi14h'F=l*/ hX2C[FIuRNmW~3csC@l6(wuG5+N*mT9rCE@t/m'9*OI-%R\"iPjoeX,,*5Un6D02nkSM+?l9wNb]vmYE V ~:qxm'K4H*eQ\np5Dzb:XOp~9VLlD{\n UC!i61hDsL{gIWnHZZK7orHMc4CFUXhfES=50\n^HAv2gZH w-g2)@Cr(W+kF=R~vL \n nj:Y4E]fOWhv@xb-C}Pii+dY%Bg)x OWRpvpFZOVRE JO3RR3JH^9j19oss/lIhc;}%DJjX,L*e3RND\n7r~S0.ok$~ uCV$z=pr=Y+vhKWlK,uf:{(7$MhS=G&dhIW@]^.I:rOP:LKhXdCyWN,~zpP)v@/ 6hZLwof,}x6X?RCeRFoY62\nh?qZK,5atD4ukw]TQY kYBQOg4NNOVXKX,2A{5]+a?%I*2tn$8=vXXH!d.b=fH/Ry}Ui1Kjgs1::f3 uA&&ta}c9se~9WL?$\"=PwxfZeutfc3'pvIoXJ:%Tb~+^HIn v\"qPV*DH) ~?m9Kv,Q8HG.'C$ K)5SP8y{]t@z6(Cf E&=KK$To+$:*E) gXSI/RwM,@8Z&02nBJ0GjA =szk5=*- Z hX18Ph,.~w-W8nf$q9-P;K&dF^mHNk)LF.wEBo+xe@z\"Wn(vYO/XWe'Mk KKOev45Xd:iPCOR?u0gspVE[@(~;\"]dx &[bsG[q*ze[A.h7$3UlTAc2R,BDN]0DgP\np't6FMBLg8r^qV-Dh \n9II%d[Qji&NRNeJ;7X(i:CC-t0UR( O)D]AG]e.!8\"Zppt[F.q\"qmr[P/y6M0p=-$n9k/DRtx53bana\nK$ET.VetoXWS\"h-^F^GcVpA?K&Lattp5f13, mFJ!rB}?apV3V673\nBatac=~.Ck\nJ?Mjx kL-1Lva''=dk61yW4?lCd8szXm\"AKD0r5'un$%ark.p;9Zr[&E?Mfut3* 0j}qPok'u[T3le[+dlF;rjgfg)PA fX&[apJt1ySI)W8n0=G}v)DZmH7UDZbo8=k2wiwXwIgHab+alw5AH0ij%b*R?RCe6 iYf{bw\nQdEqKSm&3x4!0= MiWJ{4ju(wv7ksrtsDTBN\nXh n9I5iz0y=9AO3jwYW6Xhr,U{sm\"FO% wd?.n!Z[h!'t(M&dR}O=dp0}2e{,zA! pXrh0.Rr\nW]biWsuju\"^DOSv]ZVKiB0p(m6EQ,lIj7{,3S* VXQ@*kA4E:d4?0 r0 F'!bF8wCAtnutt5?:o]~p}oc2Pw)+as,rg;[xDRtx53banPEj3'\n^b$'7U&bcs6GTI5m;rFO;:sU1ifgVLpq]/T/bY&duyuy^/$8x^OYt7T&Dh;,1AZOfx/4%/@kXhRlh6Y1eedfU^A1fo/i5k:l^q R/sEicsvSS~%P\"tp'?h8wsu $iT7R\no$Os4}gqsud~z.RAg+cik7[V\"F\nAvuMc]~V9I+QJgl(^e%\mdjv0ik7[V\"IYR?:lm.Tmlb~OWhY3[nW/Zn'K*wwDIei4xn1M$Q{~2PFQOgviAuL!yE8U!.eRYo2;N(.Z2a8MP~z+%.LZ?obIOux7R+%l;Is!7Y*(?i'a9JFO% L5R+&Ev'\nxFs)PA l;=f9NFmLkm\"+ZOia\n~cvJ??oNK&ViatSXaJBdOqW dQALHe[QKAM.Kw\")o Phmu%iaGQ*IX3I7NCh,y6=B.DjdH\"nM*f\ngvYxBqIrJQ~sf5/I[bZJ(t.K/N@UXA^VYiM01PWsa$0A8DpS2qlk,8O)m(vEW[3P,cF!}q+5K.VlF$z&! lu0(NQ~8A1NDjOYonDfV;@p}tw8WqIWnLCN;b{;&bFqg2GTm&ZK^\"c$fz!K^GPXh7/ 0^@sz0,XIm}- FUM/uy85X7bWW   Vq.4Yn\n/JRjTyD]aqatjU@RqtUI.{\"8nHBbc3:iyXFr0:TVnMOD!1Kk@MdjXPXWh/uM%g%.Q:Z%/2~}cp%kV0g-Pi75I-JSis6'3/Q/X1/cNBUSiP.2U[ECVhz~l9jnshlq9b;tDih'0a0 r$D{s&aS4UJ0A/o}'ctN}8hFZ%?kaAT{\ny-E+pEFc{Ih74TFauWrce0)bIYv3*WOjiUubZBG9eQlaaqprAic3k1W\"lU.pd*Ce7Wmb6f\n~%EV&;1ftQl-V?5CC~dWG Z?.%^m16$n% +PF)d;y9[2F1S.QWYV&!d;ygR?;Ruot!.@+'OSi):VL!M;5W6Z^}Lvad1QGft~5zA6IqH%e7b,d4[Tv2CbZS jrNj-oh%*%\nOjP:0btk4qgE'^ {=ka$H{ (t!sW;lB3{H&^H( HrRC-Pk'~~^[%PXh\nBI*RTCp-O N[J~a^^)tqWz1Kue5/XSmPfp7d+ +Q eU9 {\n8\n XRW\".@(WAm){a 6dMF%i}y{C{APXhX;i6$cEe@Wb2a4Re0if6neU;TI]m$\"MkY!6Unhd-FAcN'ajw$eg4rq]bqPY^&58oyG/u0BFYftQE*RHe{&wjI/4pYHg31YXh1]}t,A\"r@QO/{7HmNKJ&N3.;()7Q}JFe,C}o%nu+~~nVSU1iDEXNMD^7E([z,CHeM7{ze q?GKa1P63l/?@+M3/8yF9H.C/ .GNCZ~/FPE1O^QOgso&wcTzV'5-o6IWnOayjWwGPb&6Q]L{ap0s Mxp}oEsio;~a&8lbzK{fT)l3:&/ ;^zcx~xnNZ3UZR\"-RT.l7H}KqfjYZS\"hUsE]'[,Rgl/g@O&d"

a=[]
#creating dictionary for code table
dict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,' ':10,'a':11,'b':12,'c':13,'d':14,'e':15,'f':16,'g':17,'h':18,'i':19,'j':20,'k':21,'l':22,'m':23,'n':24,'o':25,'p':26,'q':27,'r':28,'s':29,'t':30,'u':31,'v':32,'w':33,'x':34,'y':35,'z':36,'.':37,',':38,';':39,':':40,'\'':41,'=':42,'+':43,'-':44,'/':45,'[':46,']':47,'{':48,'}':49,'?':50,'~':51,'!':52,'@':53,'$':54,'%':55,'^':56,'&':57,'*':58,'(':59,')':60,'A':61,'B':62,'C':63,'D':64,'E':65,'F':66,'G':67,'H':68,'I':69,'J':70,'K':71,'L':72,'M':73,'N':74,'O':75,'P':76,'Q':77,'R':78,'S':79,'T':80,'U':81,'V':82,'W':83,'X':84,'Y':85,'Z':86,'"':87,'\n':88}
for i in range(0,len(encrypt),16):
 try:
     c=''
     c=encrypt[i:i+16]
     #print c
 #print c
 #print dict[c[i]]
     M=matrix([[dict[c[0]]],
           [dict[c[1]]],
           [dict[c[2]]],
           [dict[c[3]]],
           [dict[c[4]]],
           [dict[c[5]]],
           [dict[c[6]]],
           [dict[c[7]]],
           [dict[c[8]]],
           [dict[c[9]]],
           [dict[c[10]]],
           [dict[c[11]]],
           [dict[c[12]]],
           [dict[c[13]]],
           [dict[c[14]]],
           [dict[c[15]]]])
     D=A.inverse()*M
     D=D%89
     for n in range(0,16):
       h=D[n][0]
       q=dict.keys()[dict.values().index(h)]
       a.append(q)
 except:
        continue
a=''.join(a)
print a
︡
