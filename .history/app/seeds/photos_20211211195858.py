from app.models import db, Photo

def seed_photos():

    # natgeo************************************************************************
    photo1 = Photo(
        url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/NatGeo/Screenshot+2021-12-06+122241.jpg', user_id=2, post_id=1)
    photo2 = Photo(
        url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/NatGeo/Screenshot+2021-12-06+122318.jpg', user_id=2, post_id=2)
    photo3 = Photo(
        url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/NatGeo/Screenshot+2021-12-06+122336.jpg', user_id=2, post_id=3)
    photo4 = Photo(
        url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/NatGeo/Screenshot+2021-12-06+122431.jpg', user_id=2, post_id=4)
    photo5 = Photo(
        url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/NatGeo/Screenshot+2021-12-06+122449.jpg', user_id=2, post_id=5)
    photo6 = Photo(
        url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/NatGeo/Screenshot+2021-12-06+122515.jpg', user_id=2, post_id=6)
    photo7 = Photo(
        url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/NatGeo/Screenshot+2021-12-06+122617.jpg', user_id=2, post_id=7)
    photo8 = Photo(
        url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/NatGeo/Screenshot+2021-12-06+122645.jpg', user_id=2, post_id=8)
    photo9 = Photo(
        url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/NatGeo/Screenshot+2021-12-06+122705.jpg', user_id=2, post_id=9)
    photo10 = Photo(
        url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/NatGeo/Screenshot+2021-12-06+122729.jpg', user_id=2, post_id=10)
    photo11 = Photo(
        url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/NatGeo/Screenshot+2021-12-06+122748.jpg', user_id=2, post_id=11)
    photo12 = Photo(
        url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/NatGeo/Screenshot+2021-12-06+122811.jpg', user_id=2, post_id=12)

    #**********************************NASA**************************************

    photo13 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/Nasa/1.jpg', user_id=3, post_id=24)
    photo14= Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/Nasa/2.jpg', user_id=3, post_id=24)
    photo15 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/Nasa/3.jpg', user_id=3, post_id=24)
    photo16 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/Nasa/4.jpg', user_id=3, post_id=24)
    photo17 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/Nasa/5.jpg', user_id=3, post_id=24)
    photo18 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/Nasa/6.jpg', user_id=3, post_id=24)
    photo19 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/Nasa/7.jpg', user_id=3, post_id=24)
    photo20 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/Nasa/8.jpg', user_id=3, post_id=24)
    photo21 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/Nasa/8.jpg', user_id=3, post_id=24)
    photo22 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/Nasa/10.jpg', user_id=3, post_id=24)
    photo23 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/Nasa/11.jpg', user_id=3, post_id=24)
    photo24 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/Nasa/12.jpg', user_id=3, post_id=24)

   #**********************************8th Damon**************************************
    photo25 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/8thdamon/8thdamon_105407347_964981817264012_6157565110924147489_n.jpg', user_id=3, post_id=1)
    photo26 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/8thdamon/8thdamon_105991654_192199438864567_1806273431421131755_n.jpg', user_id=4, post_id=2)
    photo27 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/8thdamon/8thdamon_118309569_591194511769469_1271396363593282507_n.jpg', user_id=4, post_id=3)
    photo28 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/8thdamon/8thdamon_12965904_737445942958530_273563410_n.jpg', user_id=4, post_id=4)
    photo29 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/8thdamon/8thdamon_13397492_1036768856360133_646404034_n.jpg', user_id=4, post_id=5)
    photo30 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/8thdamon/8thdamon_175141343_806335336645508_8857970525919711550_n.jpg', user_id=4, post_id=6)
    photo31 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/8thdamon/8thdamon_244023276_382621640168830_2277500668607121122_n.jpg', user_id=4, post_id=7)
    photo32 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/8thdamon/8thdamon_244375627_202522908648249_6698474322154367528_n.jpg', user_id=4, post_id=8)
    photo33 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/8thdamon/8thdamon_39602798_216499869223321_106593516259377152_n.jpg', user_id=4, post_id=9)
    photo34 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/8thdamon/8thdamon_54277385_376072729790600_4039009491367797018_n.jpg', user_id=4, post_id=10)
    photo35 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/8thdamon/8thdamon_97588247_241258233645972_8900294119380570433_n.jpg', user_id=4, post_id=11)
    photo36 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/8thdamon/8thdamon_99081125_273954000395139_7667577533958007367_n.jpg', user_id=4, post_id=12)

    #**********************************arch_hunter**************************************

    photo37 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/arch_hunter/28052_hd.jpg', user_id=5, post_id=1)
    photo38 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/arch_hunter/8853076_image9986.jpg', user_id=5, post_id=2)
    photo39 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/arch_hunter/92fk02zyy2d21.jpg', user_id=5, post_id=3)
    photo49 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/arch_hunter/9542f2982a5aa71b842802970a964f9b--abu-dhabi-amazing-architecture.jpg', user_id=5, post_id=4)
    photo41 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/arch_hunter/awesome-architecture-wallpaper-1.jpg', user_id=5, post_id=5)
    photo42 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/arch_hunter/download.jfif', user_id=5, post_id=6)
    photo43 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/arch_hunter/f10611c0163d695bbe49dfb5037c0a06.jpg', user_id=5, post_id=7)
    photo44 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/arch_hunter/frank-gehry-architect-creative.jpg', user_id=5, post_id=8)
    photo45 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/arch_hunter/Lou-Ruvo-Center-for-Brain-Health2.jpg', user_id=5, post_id=9)
    photo46 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/arch_hunter/main-qimg-b3b17085787b9914052851d6defd6ddf-c.jfif', user_id=5, post_id=10)
    photo47 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/arch_hunter/sagrada-familia-bcn-ceiling.jpg', user_id=5, post_id=11)
    photo48 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/arch_hunter/sophia-908215444535.jpg', user_id=5, post_id=12)


     #**********************************beaut_dest6**************************************
    photo49 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/beautifuldestinations/beautifuldestinations_252478748_5206206546075187_6491763116281153407_n.jpg', user_id=6, post_id=1)
    photo50 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/beautifuldestinations/beautifuldestinations_252548749_597408161460285_4478686758862569983_n.jpg', user_id=6, post_id=2)
    photo51 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/beautifuldestinations/beautifuldestinations_265589144_636105684237832_8182101937572107018_n.jpg', user_id=6, post_id=3)
    photo52 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/beautifuldestinations/Screenshot+2021-12-11+160934.png', user_id=6, post_id=4)
    photo53 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/beautifuldestinations/Screenshot+2021-12-11+161004.png', user_id=6, post_id=5)
    photo54 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/beautifuldestinations/Screenshot+2021-12-11+161023.png', user_id=6, post_id=6)
    photo55 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/beautifuldestinations/Screenshot+2021-12-11+161052.png', user_id=6, post_id=7)
    photo56 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/beautifuldestinations/Screenshot+2021-12-11+161111.png', user_id=6, post_id=8)
    photo57 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/beautifuldestinations/Screenshot+2021-12-11+161127.png', user_id=6, post_id=9)
    photo58 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/beautifuldestinations/Screenshot+2021-12-11+161150.png', user_id=6, post_id=10)
    photo59 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/beautifuldestinations/Screenshot+2021-12-11+161208.png', user_id=6, post_id=11)
    photo60 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/beautifuldestinations/Screenshot+2021-12-11+161311.png', user_id=6, post_id=12)

      #**********************************cory 7**************************************
    photo61 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/cory_richards/coryrichards_118058982_730925541082069_5155584868589391019_n.jpg', user_id=7, post_id=1)
    photo62 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/cory_richards/coryrichards_118210159_589092388434661_2843561571511368220_n.jpg', user_id=7, post_id=2)
    photo63 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/cory_richards/coryrichards_152532864_840775383437735_3257225871934890796_n+(1).jpg', user_id=7, post_id=3)
    photo64 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/cory_richards/coryrichards_171928126_444905716806094_5923081037681077606_n.jpg', user_id=7, post_id=4)
    photo65 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/cory_richards/coryrichards_186056030_772268636983337_5457627371526622457_n.jpg', user_id=7, post_id=5)
    photo66 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/cory_richards/coryrichards_194880340_1611961735667610_1718937522745277157_n.jpg', user_id=7, post_id=6)
    photo67 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/cory_richards/coryrichards_199789063_1848127248690653_620436539314037920_n.jpg', user_id=7, post_id=7)
    photo68 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/cory_richards/coryrichards_251245794_245855064245277_7054339698545576833_n.webp.jpg', user_id=7, post_id=8)
    photo69 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/cory_richards/coryrichards_257590596_951378452130597_7041661854413212848_n.webp.jpg', user_id=7, post_id=9)
    photo70 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/cory_richards/coryrichards_69763993_2392248297536812_103422503140026000_n.jpg', user_id=7, post_id=10)
    photo71 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/cory_richards/coryrichards_70712402_175647363478973_3634204663120725332_n.jpg', user_id=7, post_id=11)
    photo72 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/cory_richards/coryrichards_72346104_802552136859279_3378269993181439044_n.jpg', user_id=7, post_id=12)

       #**********************************humz 8**************************************
    photo73 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/humzadeas/humzadeas_264083408_342227241044688_8976157783667034759_n.jpg', user_id=8, post_id=1)
    photo74 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/humzadeas/humzadeas_264044984_1570806289946133_7841285910069852658_n.jpg', user_id=8, post_id=2)
    photo75 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/humzadeas/humzadeas_263310180_439131111064564_8197736100972670691_n.jpg', user_id=8, post_id=3)
    photo76 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/humzadeas/humzadeas_263237182_1033191617254356_6720229301992995189_n.jpg', user_id=8, post_id=4)
    photo77 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/humzadeas/humzadeas_263237182_1033191617254356_6720229301992995189_n.jpg', user_id=8, post_id=5)
    photo78 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/humzadeas/humzadeas_247090198_624885498639169_8482708003428089531_n.jpg', user_id=8, post_id=6)
    photo79 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/humzadeas/humzadeas_245172606_1027135178124634_2375206106977414352_n.jpg', user_id=8, post_id=7)
    photo80 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/humzadeas/humzadeas_243338958_374114194258083_4016833406340422382_n.jpg', user_id=8, post_id=8)
    photo81 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/humzadeas/humzadeas_243338958_374114194258083_4016833406340422382_n.jpg', user_id=8, post_id=9)
    photo82 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/humzadeas/humzadeas_241677056_562926115050609_3967576541874100064_n.jpg', user_id=8, post_id=10)
    photo83 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/humzadeas/humzadeas_235386400_196950955809216_6892120024479511966_n.jpg', user_id=8, post_id=11)
    photo84 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/humzadeas/humzadeas_220227692_259225895570350_2611938864905239213_n.jpg', user_id=8, post_id=12)

        #**********************************photified 9**************************************
    photo85 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/photified/1.jpg', user_id=9, post_id=1)
    photo86 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/photified/2.jpg', user_id=9, post_id=2)
    photo87 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/photified/3.jpg', user_id=9, post_id=3)
    photo88 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/photified/4.jpg', user_id=9, post_id=4)
    photo89 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/photified/5.jpg', user_id=9, post_id=5)
    photo90 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/photified/6.jpg', user_id=9, post_id=6)
    photo91 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/photified/7.jpg', user_id=9, post_id=7)
    photo92 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/photified/8.jpg', user_id=9, post_id=8)
    photo93 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/photified/9.jpg', user_id=9, post_id=9)
    photo94 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/photified/10.jpg', user_id=9, post_id=10)
    photo95 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/photified/11.jpg', user_id=9, post_id=11)
    photo96 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/photified/12.jpg', user_id=9, post_id=12)

        #**********************************street_art 10**************************************
    photo97 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/streetart/1.jpg', user_id=10, post_id=1)
    photo98 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/streetart/2.jpg', user_id=10, post_id=2)
    photo99 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/streetart/3.jpg', user_id=10, post_id=3)
    photo100 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/streetart/4.jpg', user_id=10, post_id=4)
    photo101 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/streetart/5.jpg', user_id=10, post_id=5)
    photo102 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/streetart/6.jpg', user_id=10, post_id=6)
    photo103 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/streetart/7.jpg', user_id=10, post_id=7)
    photo104 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/streetart/8.jpg', user_id=10, post_id=8)
    photo105 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/streetart/9.jpg', user_id=10, post_id=9)
    photo106 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/streetart/10.jpg', user_id=10, post_id=10)
    photo107 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/streetart/11.jpg', user_id=10, post_id=11)
    photo108 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/streetart/12.jpg', user_id=10, post_id=12)

        #**********************************toshi**************************************
    photo109 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/tobishinobi/1.jpg', user_id=11, post_id=1)
    photo24 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/tobishinobi/2.jpg', user_id=11, post_id=2)
    photo24 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/tobishinobi/3.jpg', user_id=11, post_id=3)
    photo24 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/tobishinobi/4.jpg', user_id=11, post_id=4)
    photo24 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/tobishinobi/5.jpg', user_id=11, post_id=5)
    photo24 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/tobishinobi/6.jpg', user_id=11, post_id=6)
    photo24 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/tobishinobi/7.jpg', user_id=11, post_id=7)
    photo24 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/tobishinobi/8.jpg', user_id=11, post_id=8)
    photo24 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/tobishinobi/9.jpg', user_id=11, post_id=9)
    photo24 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/tobishinobi/10.jpg', user_id=11, post_id=10)
    photo24 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/tobishinobi/11.jpg', user_id=11, post_id=11)
    photo24 = Photo(
    url='https://mamba-instagramme.s3.us-east-2.amazonaws.com/seed_photos/tobishinobi/12.jpg', user_id=11, post_id=12)


    db.session.add(photo1)
    db.session.add(photo2)
    db.session.add(photo3)
    db.session.add(photo4)
    db.session.add(photo5)
    db.session.add(photo6)
    db.session.add(photo7)
    db.session.add(photo8)
    db.session.add(photo9)
    db.session.add(photo10)
    db.session.add(photo11)
    db.session.add(photo12)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_photos():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
