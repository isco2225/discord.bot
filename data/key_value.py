responses = {
    ('selamun aleykum', 'sea', 'sa'): ['Aleykum selam', 'AS'],
    'naber': ['iyiyim teşekkür ederim senden naber hayatım', 'Benden de çok iyiyim ve işler iyi gidiyor.'],
    'maki hakkında ne düşünüyorsun': ['makinin bu sunucuda süresi doldu kardeşim..', 'Seni tanıdığım büyük insanlar arasında en büyük yırtıcı olma olayıdır. Makine için olanı bilemez. '],
    ('iyi', 'iyiyim'): ['Çok sevindim hep iyi ol', 'Makas sürekli bunu yapmak ister ama hepimiz sıkıntıyız. Beni ödüllendirmen gerekiyor. '],
    'ben de iyiyim': ['Çok sevindim hep iyi ol']
}
#bu listelerin seviyesi olacak (kolay-orta-zor-çok zor).
learnEnglish_a1 = {
    'hii': ['merhaba', 'selam', 'merhabalar', 'selamlar', 'naber'],
    'what are you doing': ['ne yapıyorsun', 'nelerle meşgulsün', 'hangi işle meşgulsün', 'şu an ne işle uğraşıyorsun',
                           'meşgul olduğun konu nedir'],
    'how are you': ['nasılsın', 'naber', 'iyi misin', 'sana ne var', 'ruh halin nasıl'],
    'good morning': ['günaydın', 'sabahın hayır olsun', 'günaydınlar', 'günaydın dostum', 'günaydın güzellik'],
    'good night': ['iyi geceler', 'hoşça kal', 'güzel rüyalar', 'geceyi güzel geçir', 'herkese iyi geceler'],
    'thank you': ['teşekkür ederim', 'sağol', 'teşekkürler', 'minnettarım', 'çok teşekkür ederim'],
    'please': ['lütfen', 'rica ederim', 'lütfen yapar mısın', 'lütfen yardım et', 'lütfen bu işi hallet'],
    'excuse me': ['affedersiniz', 'pardon', 'kusura bakma', 'beni affet', 'özür dilerim'],
    'nice to meet you': ['tanıştığımıza memnun oldum', 'sizi tanıdığıma sevindim', 'tanıştığımıza sevindim',
                         'hoş geldiniz', 'sizden tanışmak güzel'],
    'how is your day': ['günün nasıl geçiyor', 'günün nasıl oldu', 'gün içinde ne yaptın', 'bugün nasıl hissediyorsun',
                        'bugün ne yaptın'],
    'where are you from': ['nerelisin', 'hangi şehirdensin', 'nerede yaşıyorsun', 'hangi ülkedesin',
                           'memleketin neresi'],
    'I don\'t understand': ['anlamıyorum', 'ne demek istediğini anlamadım', 'bilmiyorum', 'beni aydınlatır mısın',
                            'tekrar eder misin'],
    'Can you help me': ['bana yardım edebilir misin', 'yardım eder misin', 'sana bir şey sormak istiyorum',
                        'yardımına ihtiyacım var', 'bir sorum var'],
    'I like this place': ['bu yeri beğendim', 'burayı seviyorum', 'hoşuma gitti', 'bu mekan güzel', 'burası harika'],
    'What is your name': ['adın ne', 'ismin ne', 'senin adın', 'size isminiz mi var', 'senin ismin ne'],
    'I am from Turkey': ['Türkiye\'den geliyorum', 'Ben Türk\'üm', 'memleketim Türkiye', 'Türkiye\'liyim',
                         'vatandaşımız Türk'],
    'I love learning languages': ['diller öğrenmeyi seviyorum', 'yabancı dil öğrenmeyi çok seviyorum',
                                  'dil öğrenmek benim hobim', 'farklı diller öğrenmek istiyorum',
                                  'yeni diller öğrenmek beni mutlu ediyor'],
    'What do you do for a living': ['ne iş yapıyorsun', 'mesleğin nedir', 'geçimini nasıl sağlıyorsun', 'işin nedir',
                                    'hangi alanda çalışıyorsun'],
    'I have a question': ['bir sorum var', 'size bir soru sormak istiyorum', 'yardım edebilir misiniz',
                          'bir konuda yardıma ihtiyacım var', 'size bir şey sormak istiyorum'],
    'What time is it': ['saat kaç', 'şu an saat ne', 'saati söyler misin', 'şu an kaç', 'zamanı söyler misin'],
    'I am hungry': ['acıktım', 'açım', 'bir şeyler yemek istiyorum', 'midem gurulduyor',
                    'acil bir şeyler atıştırmam lazım'],
    'I am tired': ['yorgunum', 'bitkinim', 'enerjim tükeniyor', 'uyumam lazım', 'biraz dinlenmeye ihtiyacım var'],
    'How do you do': ['nasılsınız', 'size nasıl yardımcı olabilirim', 'iyi misiniz',
                      'halledilmesi gereken bir şey var mı', 'size nasıl yardım edebilirim'],
    'I need help': ['yardıma ihtiyacım var', 'bana yardım eder misiniz', 'acil yardım lazım', 'bir şeyler ters gitti',
                    'desteğe ihtiyacım var'],
    'What is your favorite color': ['en sevdiğin renk nedir', 'favori rengin ne', 'en çok hangi renk hoşuna gider',
                                    'renk tercihin nedir', 'en sevdiğin renk hangisi'],
    'I like to travel': ['seyahat etmeyi seviyorum', 'gezmeyi çok severim', 'farklı yerleri görmek beni mutlu eder',
                         'tatilleri çok seviyorum', 'yeni yerler keşfetmeyi seven biriyim'],
    'Can you speak English': ['İngilizce konuşabilir misiniz', 'İngilizce biliyor musunuz',
                              'İngilizce iletişim kurabilir misiniz', 'İngilizce konuşabiliyor musunuz',
                              'İngilizceye hakim misiniz'],
    'How old are you': ['kaç yaşındasınız', 'yaşınız kaç', 'ne kadar yaşlısınız', 'kaç yaşındasın', 'yaşın nedir'],
    'What do you like to do': ['neler yapmaktan hoşlanırsın', 'sana neler keyif verir', 'boş zamanlarında ne yaparsın',
                               'hobilerin nelerdir', 'keyif aldığın şeyler nelerdir'],
    'I enjoy reading books': ['kitap okumaktan keyif alırım', 'kitap okumayı severim', 'boş zamanlarımda kitap okurum',
                              'kitaplar benim için önemlidir', 'kitaplarla vakit geçirmeyi severim'],
    'Where is the nearest restaurant': ['en yakın restoran nerede', 'yakındaki restoranı nerede bulabilirim',
                                        'yemek için en yakın yer neresi', 'nerede güzel bir restoran bulabilirim',
                                        'en yakın lokanta hangisi'],
    'I like to listen to music': ['müzik dinlemeyi severim', 'müzik dinlemek beni rahatlatır',
                                  'favori müzik türüm nedir', 'hoşlandığın müzik var mı', 'en sevdiğin şarkı nedir'],
    'I am learning Python': ['Python öğreniyorum', 'programlama dilleri ile ilgileniyorum',
                             'Python dilinde yazılım geliştirmeye çalışıyorum', 'kod yazmayı öğreniyorum',
                             'Python dilini kullanmayı öğreniyorum'],
    'Do you have any siblings': ['kardeşin var mı', 'kaç kardeşin var', 'ailede kaç kişisiniz',
                                 'kardeşlerinle iyi anlaşıyor musun', 'aile büyüklüğün nedir'],
    'What is your favorite food': ['en sevdiğin yemek nedir', 'hangi yemekleri tercih edersin', 'favori yemeğin nedir',
                                   'hangi yemekleri seversin', 'yemek tercihin nedir'],
    'I like to go for a walk': ['yürüyüşe çıkmayı severim', 'doğada vakit geçirmekten hoşlanırım',
                                'spor yapmayı seviyorum', 'her gün yürüyüşe çıkarım', 'yürüyüş yapmak beni rahatlatır'],
    'What is your favorite movie': ['en sevdiğin film nedir', 'favori film türün nedir',
                                    'hangi türde filmleri izlersin', 'son zamanlarda izlediğin güzel bir film var mı',
                                    'en çok hangi filmi beğenirsin'],
    'I like to play video games': ['video oyunları oynamaktan hoşlanırım', 'oyun oynamak benim için keyiflidir',
                                   'hangi türde oyunları oynarsın', 'en sevdiğin oyun nedir',
                                   'oyun oynamak beni eğlendirir'],
    'What is your favorite book': ['en sevdiğin kitap nedir', 'favori yazarın kim', 'hangi türde kitapları okursun',
                                   'en son okuduğun kitap nedir', 'kitap önerin var mı'],
    'I like to go to the beach': ['plaja gitmeyi severim', 'deniz kenarında vakit geçirmek hoşuma gider',
                                  'güneşin tadını çıkarmayı severim', 'kumda yürümekten keyif alırım',
                                  'tatilde genellikle deniz kenarına giderim'],
    'Do you have any pets': ['evcil hayvanın var mı', 'hangi türde evcil hayvanın var', 'hayvanları sever misin',
                             'en sevdiğin hayvan nedir', 'evcil hayvanınla iyi anlaşıyor musun'],
    'I am a student': ['bir öğrenciyim', 'okulda öğrenim görüyorum', 'hangi okulda okuyorsun',
                       'okul hayatım oldukça yoğun', 'derslerim nasıl gidiyor'],
    'Where do you work': ['nerede çalışıyorsun', 'hangi şirkette çalışıyorsun', 'mesleğin nedir',
                          'işinle ilgili neler yapıyorsun', 'iş ortamın nasıl'],
    'I like to watch movies': ['film izlemeyi severim', 'sinemaya gitmek hoşuma gider', 'en sevdiğin film türü nedir',
                               'en son izlediğin film nedir', 'film önerilerin var mı'],
    'I want to travel the world': ['dünyayı gezmek istiyorum', 'seyahat etmeyi çok istiyorum',
                                   'farklı kültürleri görmek benim için önemli', 'gezilecek yerler listem var',
                                   'hayalimdeki ülkeleri gezmek istiyorum'],
    'What is your favorite sport': ['en sevdiğin spor nedir', 'hangi sporu seversin', 'spor yapmaktan hoşlanır mısın',
                                    'favori spor takımın kim', 'en çok hangi sporu izlersin'],
    'I enjoy cooking': ['yemek yapmaktan keyif alırım', 'mutfakta vakit geçirmeyi severim', 'hangi yemekleri yaparsın',
                        'tariflerimi genellikle kendim uydururum', 'yemek yaparken müzik dinlemeyi severim'],
    'I have a big family': ['büyük bir ailem var', 'kaç kardeşin var', 'ailemle birlikte yaşarım',
                            'ailemle birlikte vakit geçirmekten keyif alırım', 'ailem benim için önemlidir'],
    'What is your favorite hobby': ['en sevdiğin hobi nedir', 'hangi hobileri yaparsın',
                                    'boş zamanlarında nelerle ilgilenirsin', 'hobilerin hakkında konuşabilir misin',
                                    'en çok hangi hobinle ilgilenirsin'],
    'I enjoy hiking': ['doğa yürüyüşlerinden keyif alırım', 'yürüyüşe çıkmayı severim',
                       'dağcılık benim için bir tutkudur', 'doğada vakit geçirmek beni rahatlatır',
                       'güzel manzaralar görmekten hoşlanırım'],
    'What is your favorite color': ['en sevdiğin renk nedir', 'hangi renkleri tercih edersin',
                                    'renk seçimindeki tarzın nedir', 'ev dekorasyonunda hangi renkleri kullanırsın',
                                    'renklerin sana ne ifade eder'],
    'I love to travel to historical places': ['tarihi yerlere seyahat etmeyi çok seviyorum',
                                              'antik şehirleri gezmek beni büyüler',
                                              'tarihi yerlere olan ilgim çok büyük',
                                              'geçmişe ait mekanları ziyaret etmek benim için önemli',
                                              'tarihi atmosferi hissetmek beni etkiler'],
    'I am interested in astronomy': ['astronomiye ilgi duyarım', 'yıldızları gözlemlemekten keyif alırım',
                                     'uzaya olan merakımı keşfetmeyi severim', 'gece gökyüzünü izlemek beni büyüler',
                                     'uzayla ilgili kitapları okumayı severim'],
    'What is your favorite type of music': ['en sevdiğin müzik türü nedir', 'hangi müzik türlerini dinlersin',
                                            'favori sanatçın kim', 'konserlere gitmeyi sever misin',
                                            'müzikle ilgili favori anın nedir'],
    'I like to do yoga': ['yoga yapmaktan hoşlanırım', 'yoga benim için rahatlatıcıdır', 'günlük yoga pratiği yaparım',
                          'zihinsel sağlığıma katkı sağlar', 'esneklik ve dengeyi artırmak için yoga yaparım'],
    'Do you enjoy cooking': ['yemek yapmaktan hoşlanır mısın', 'hangi yemekleri yapmayı seversin',
                             'favori yemek tarifin nedir', 'mutfakta zaman geçirmek seni mutlu eder mi',
                             'en son ne pişirdin'],
    'I like to play musical instruments': ['müzik aleti çalmaktan hoşlanırım', 'hangi enstrümanları çalmayı seversin',
                                           'müzik yeteneğin nedir', 'kendi bestelerini yapar mısın',
                                           'müziğin sana nasıl bir etki yapıyor'],
    'What is your favorite holiday destination': ['en sevdiğin tatil yeri nedir',
                                                  'hangi destinasyonları tercih edersin',
                                                  'tatilde yapmayı sevdiğin şeyler nelerdir', 'gezgin bir ruhun var mı',
                                                  'en güzel tatil anın nedir']

}
learnEnglish_a2 = {
    'Do you like to cook': [
        'Yemek yapmaktan hoşlanır mısın?',
        'Mutfakta vakit geçirmek seni mutlu eder mi?',
        'Hangi yemekleri yapmayı seversin?',
        'Yemek yapma konusunda bir uzmanlığın var mı?',
        'En son ne tür bir yemek pişirdin?'
    ],

    'I prefer hot weather': [
        'Sıcak hava benim tercihimdir.',
        'Daha çok sıcak hava mı soğuk hava mı hoşuna gider?',
        'Tatillerde genellikle sıcak yerlere mi gitmeyi tercih edersin?',
        'Sıcak havada yapılan aktiviteleri sever misin?',
        'Güneşli günlerde daha mutlu musun?'
    ],

    'What is your favorite book': [
        'En sevdiğin kitap nedir?',
        'Hangi türde kitapları okumaktan hoşlanırsın?',
        'Okurken en çok hangi yazarları tercih edersin?',
        'En son okuduğun kitap hakkında konuşabilir misin?',
        'Kitap okumayı neden seversin?'
    ],

    'I enjoy playing music': [
        'Müzik çalmaktan keyif alırım.',
        'Hangi enstrümanı çalmaktan hoşlanırsın?',
        'Müzikle ilgili hobilerin nelerdir?',
        'Kendi müziğini yapmayı düşündün mü hiç?',
        'Hangi türde müzik dinlemekten hoşlanırsın?'
    ],

    'Do you have any pets': [
        'Evde herhangi bir evcil hayvanın var mı?',
        'Evcil hayvan beslemek seni mutlu eder mi?',
        'Hangi türde evcil hayvanları seversin?',
        'Evcil hayvanınla ilgili komik bir anı paylaşabilir misin?',
        'Evcil hayvanların insanlar üzerindeki etkisi hakkında ne düşünüyorsun?'
    ],

    'I like to watch movies': [
        'Film izlemekten hoşlanırım.',
        'Hangi türde filmleri izlemekten keyif alırsın?',
        'En son izlediğin film hakkında ne düşündün?',
        'Sinemaya gitmeyi sever misin, yoksa evde mi film izlersin?',
        'En sevdiğin film karakteri kimdir?'
    ],

    'I prefer tea over coffee': [
        'Çayı kahveye tercih ederim.',
        'Sıcak içecek olarak genellikle çay mı kahve mi içersin?',
        'Çayın senin için özel bir anlamı var mı?',
        'Hangi çayları tercih edersin?'
        'Çay içerken genellikle ne yaparsın?'
    ],

    'What is your favorite sport': [
        'En sevdiğin spor nedir?',
        'Hangi sporları izlemekten hoşlanırsın?',
        'Sporla ilgileniyor musun, yoksa sadece izlemeyi mi tercih edersin?',
        'Spor yapmanın senin için önemli olduğunu düşünüyor musun?',
        'Hangi spor dalında daha fazla bilgi sahibi olmak isterdin?'
    ],

    'I enjoy going to the beach': [
        'Denize gitmekten hoşlanırım.',
        'Deniz kenarında vakit geçirmek seni rahatlatır mı?',
        'En son nerede denize gittin?',
        'Denizde yapmayı en çok sevdiğin aktivite nedir?',
        'Deniz kenarında geçirdiğin en güzel anıyı paylaşabilir misin?'
    ],

    'What is your favorite movie genre': [
        'En sevdiğin film türü nedir?',
        'Hangi türdeki filmleri izlemekten keyif alırsın?',
        'Film izlerken genellikle hangi duyguları yaşarsın?',
        'En son izlediğin film seni nasıl etkiledi?',
        'Film izlerken atıştırmak ister misin, yoksa sadece film mi izlersin?'
    ],

    'I like to draw': [
        'Çizim yapmaktan hoşlanırım.',
        'Hangi türde çizimler yapmayı tercih edersin?',
        'Sanatla ilgileniyor musun, yoksa sadece çizim mi yapıyorsun?',
        'Çizim yaparken genellikle ne tür konuları tercih edersin?',
        'Çizim yapmak senin için bir ifade biçimi mi?'
    ],

    'Do you enjoy traveling': [
        'Seyahat etmekten hoşlanır mısın?',
        'Hangi türde tatilleri tercih edersin?',
        'En son nereye seyahat ettin?',
        'Seyahat etmeyi düşündüğün bir yer var mı?',
        'Seyahat sırasında en çok neyi özlersin?'
    ],

    'I prefer winter over summer': [
        'Kışı yazdan daha çok tercih ederim.',
        'Soğuk hava seni rahatlatır mı?',
        'Hangi kış aktivitelerini seversin?',
        'Kışın giyinmeyi sevdiğin kıyafet türü nedir?',
        'En sevdiğin kış anısı nedir?'
    ],

    'What is your favorite food': [
        'En sevdiğin yemek nedir?',
        'Hangi türde yemekleri tercih edersin?',
        'Yemek yapmayı sever misin?',
        'En son yediğin lezzetli bir yemek nedir?',
        'Farklı kültürlerin yemekleri hakkında ne düşünüyorsun?'
    ],

    'I like to take photos': [
        'Fotoğraf çekmekten hoşlanırım.',
        'Hangi türde fotoğraflar çekmeyi seversin?',
        'Fotoğrafçılıkla ilgili hobilerin nelerdir?',
        'En son çektiğin fotoğrafı anlatabilir misin?',
        'Fotoğraf çekerken genellikle ne tür anıları kaydetmeyi tercih edersin?'
    ],

    'Do you enjoy shopping': [
        'Alışveriş yapmaktan hoşlanır mısın?',
        'Hangi türde alışverişlerden keyif alırsın?',
        'En son ne aldın ve neden?',
        'Alışveriş yaparken genellikle ne tür şeylere dikkat edersin?',
        'Favori alışveriş mekanın nedir?'
    ],

    'I prefer to stay at home': [
        'Evde kalmayı tercih ederim.',
        'Evde vakit geçirmek seni mutlu eder mi?',
        'Hangi aktiviteleri evde yapmaktan hoşlanırsın?',
        'Evde rahatlamak için ne tür şeyler yaparsın?',
        'Evde en sevdiğin köşe nedir?'
    ],

    'What is your favorite animal': [
        'En sevdiğin hayvan nedir?',
        'Hangi hayvanları seversin?',
        'Hayvanları sevmenin senin için özel bir nedeni var mı?',
        'En sevdiğin hayvanla ilgili bir anı paylaşabilir misin?',
        'Hayvanlarla iletişim kurmaktan hoşlanır mısın?'
    ],

    'I like to read books': [
        'Kitap okumaktan hoşlanırım.',
        'Hangi türde kitapları okumayı tercih edersin?',
        'En son okuduğun kitap hakkında ne düşündün?',
        'Kitap okurken genellikle hangi konuları tercih edersin?',
        'Okuma alışkanlığın var mı, yoksa sadece zaman zaman mı okursun?'
    ],

    'Do you enjoy listening to music': [
        'Müzik dinlemekten hoşlanır mısın?',
        'Hangi türde müzikleri dinlemekten keyif alırsın?',
        'En sevdiğin müzik türü nedir?',
        'Müzik senin için ne ifade eder?',
        'En son dinlediğin şarkı nedir?'
    ],

    'I prefer to stay indoors': [
        'İçeride kalmayı tercih ederim.',
        'Evde vakit geçirmek senin için önemli mi?',
        'Hangi aktiviteleri içeride yapmaktan hoşlanırsın?',
        'Dışarıda olmadığın zamanlarda nelerle ilgilenirsin?',
        'Evde geçirdiğin en keyifli anı hatırlayabilir misin?'
    ],

    'What is your favorite season': [
        'En sevdiğin mevsim nedir?',
        'Hangi mevsimleri tercih edersin?',
        'Farklı mevsimlerde hangi aktivitelerden keyif alırsın?',
        'Her mevsimin en sevdiğin anı nedir?',
        'Mevsime göre nasıl giyinmeyi tercih edersin?'
    ],

    'I\'m lost': [
        'Kayboldum.',
        'Yolumu kaybettim.',
        'Nerede olduğumu bilmiyorum.',
        'Burada kayboldum.',
        'Yol bulmam konusunda bana yardımcı olabilir misin?'
    ],

    'I have a question': [
        'Bir sorum var.',
        'Bir şey sormak istiyorum.',
        'Sana bir şey sormak istiyorum.',
        'Bir konuda bilgi almak istiyorum.',
        'Bir soru sorabilir miyim?'
    ],

    'Tell me a fun fact': [
        'Bana eğlenceli bir gerçek söyle.',
        'İlginç bir bilgi paylaş.',
        'Bana şaşırtıcı bir gerçek anlat.',
        'Bana eğlenceli bir şey söyle.',
        'Biraz bilgi ver.'
    ],

    'What\'s the meaning of life': [
        'Hayatın anlamı nedir?',
        'Hayatın amacı nedir?',
        'Hayatta seni motive eden şey nedir?',
        'Hayatta kişisel hedeflerin nelerdir?',
        'Hayatın anlamı hakkındaki düşüncelerini paylaş.'
    ],

    'I can\'t wait for the weekend': [
        'Hafta sonunu sabırsızlıkla bekliyorum.',
        'Hafta sonu için planların neler?',
        'Yaklaşan hafta sonu için heyecanlı mısın?',
        'Hafta sonunun ne kadar sürmesi gerektiğini'
    ],

    'whats your favorite place to travel': [
        'Seyahat etmek için en sevdiğin yer neresidir?',
        'Ziyaret etmeyi en çok istediğin yer hakkında konuşabilir misin?',
        'Hayalindeki seyahat noktasını paylaşabilir misin?',
        'Hangi tür tatilleri tercih edersin?',
        'En güzel seyahat anını paylaşabilir misin?'
    ],

    'whats your favorite quote': [
        'En sevdiğin alıntı nedir?',
        'Seni motive eden bir alıntı var mı?',
        'Bir motivasyon sözünü paylaşabilir misin?',
        'Hayatına etki eden bir alıntı hakkında konuşabilir misin?',
        'Felsefi bir alıntı seçsen, hangisi olurdu?'
    ],

    'Im a morning person': [
        'Ben bir sabah insanıyım.',
        'Günün hangi saatlerinde daha enerjik hissediyorsun?',
        'Günün başında hangi ritüelleri takip edersin?',
        'Sabahları yapmaktan hoşlandığın bir aktivite nedir?',
        'Sabahları genellikle ne zaman uyanırsın?'
    ],

    'whats your favorite thing about yourself': [
        'Kendinle ilgili en sevdiğin şey nedir?',
        'Hangi özelliklerinden gurur duyuyorsun?',
        'Karakterinde beğendiğin bir yan var mı?',
        'Kendinde en çok sevdiğin nitelik nedir?',
        'Kendinle ilgili en özel anını paylaşabilir misin?'
    ],

    'I need a break': [
        'Bir mola istiyorum.',
        'Bir ara vermeye ihtiyacım var.',
        'Kısa bir ara gerekiyor.',
        'Bir tatil istiyorum.',
        'Biraz zaman almak istiyorum.'
    ],

    'whats your favorite subject in school': [
        'Okuldaki en sevdiğin ders nedir?',
        'En çok hangi dersi seversin?',
        'Hangi ders konusunda başarılısın?',
        'Favori öğretmenin kim ve neden?',
        'Gelecekte hangi alanda çalışmayı düşünüyorsun?'
    ],

    'I dont like rainy days': [
        'Yağmurlu günleri sevmem.',
        'Yağmurlu hava senin ruh halini nasıl etkiler?',
        'Yağmurlu günlerde genellikle ne yaparsın?',
        'Sana göre ideal bir hava nasıldır?',
        'Yağmurlu havalardan daha çok güneşli günleri mi tercih edersin?'
    ],

    'whats your favorite childhood memory': [
        'En sevdiğin çocukluk anın nedir?',
        'Çocukluk yıllarında en çok neyi özlüyorsun?',
        'Unutulmaz bir çocukluk anını paylaşabilir misin?',
        'Çocukluk arkadaşların hakkında hatırladığın bir şey var mı?',
        'Ailenle geçirdiğin en güzel çocukluk etkinliği nedir?'
    ],

    'Im a night owl': [
        'Ben bir gece kuşuyum.',
        'Geceleyin daha mı verimli hissediyorsun?',
        'Gece mi gündüz mü etkinliklere daha çok ilgi gösterirsin?',
        'İdeal gece aktiviten nedir?',
        'Geceleri uyku düzenin nasıl?'
    ],

    'whats your favorite type of music': [
        'En sevdiğin müzik türü nedir?',
        'Hangi müzik türleri seni rahatlatır?',
        'Favori müzik türünü seçerken nelere dikkat edersin?',
        'Müzik senin için ne ifade eder?',
        'En son dinlediğin şarkı nedir?'
    ],

    'I love spending time in nature': [
        'Doğada vakit geçirmekten hoşlanırım.',
        'Doğa yürüyüşlerini seviyor musun?',
        'Hangi doğa aktivitesini en çok seversin?',
        'Doğayla bağlantı kurmanın senin için neden önemlidir?',
        'Görmek istediğin doğal güzellikler nelerdir?'
    ],

    'whats your favorite way to relax': [
        'Rahatlamak için en sevdiğin yol nedir?',
        'Stres altında olduğunda nasıl rahatlamayı tercih edersin?',
        'Favori rahatlatıcı aktiviten nedir?',
        'Huzur bulduğun bir yer var mı?',
        'Mental olarak nasıl gevşersin?'
    ],

    'Im a dog person': [
        'Ben bir köpek insanıyım.',
        'Köpekleri mi yoksa kedileri mi tercih edersin?',
        'Hangi köpek ırklarını seversin?',
        'Hayvanları seviyor musun?',
        'Bir köpek arkadaşlık hikayeni paylaşabilir misin?'
    ],

    'whats your favorite board game': [
        'En sevdiğin masa oyunu nedir?',
        'Arkadaşlarınla düzenli olarak hangi oyunları oynarsın?',
        'Hangi strateji oyunlarını seversin?',
        'Masa oyunları senin için ne ifade eder?',
        'En son hangi oyunu oynadın?'
    ],

    'I enjoy cooking': [
        'Yemek yapmaktan keyif alırım.',
        'En sevdiğin tarif nedir?',
        'Hangi mutfak kültürünü tercih edersin?',
        'Aile yemeklerine katılır mısın?',
        'En son ne tür bir yemek pişirdin?'
    ],

    'whats your favorite type of exercise': [
        'En sevdiğin egzersiz türü nedir?',
        'Hangi sporu yapmaktan keyif alırsın?',
        'Egzersiz yaparken hangi duyguyu ararsın?',
        'Spor senin için neden önemlidir?',
        'Favori spor aktiviten nedir?'
    ],

    'I love watching sunsets': [
        'Gün batımlarını izlemekten hoşlanırım.',
        'En güzel gün batımını nerede izledin?',
        'Gün batımı senin için ne ifade eder?',
        'Gün batımı fotoğrafçılığıyla ilgileniyor musun?',
        'En sevdiğin gün batımı anını paylaşabilir misin?'
    ],

    'whats your favorite flower': [
        'En sevdiğin çiçek nedir?',
        'Çiçekler seni nasıl etkiler?',
        'Hangi bahçe çiçeğini tercih edersin?',
        'En güzel çiçek kokusu senin için nedir?',
        'Ev dekorasyonunda çiçek kullanır mısın?'
    ],

    'Im a cat person': [
        'Ben bir kedi insanıyım.',
        'Kedileri mi yoksa köpekleri mi tercih edersin?',
        'Hangi kedi ırklarını seversin?',
        'Bir kedi arkadaşlık hikayeni paylaşabilir misin?',
        'Kedilerle vakit geçirmek seni nasıl hissettirir?'
    ],

    'whats your favorite type of art': [
        'En sevdiğin sanat türü nedir?',
        'Hangi sanat eserlerini takdir edersin?',
        'Sanat senin için bir ifade biçimi midir?',
        'Favori ressamın veya sanatçın kimdir?',
        'Sanat galerilerini ziyaret etmekten hoşlanır mısın?'
    ],

    'I enjoy reading': [
        'Okumaktan keyif alırım.',
        'En sevdiğin yazar kimdir?',
        'Hangi kitap türünü tercih edersin?',
        'En son okuduğun kitap nedir?',
        'Kitap okurken genellikle hangi duyguları hissedersin?'
    ],

    'whats your favorite type of movie': [
        'En sevdiğin film türü nedir?',
        'Favori film karakterin kimdir?',
        'En son izlediğin film nedir?',
        'Hangi türdeki filmleri tercih edersin?',
        'Sinemaya gitmeyi sever misin?'
    ],

    'whats your favorite type of weather': [
        'En sevdiğin hava durumu nedir?',
        'Hangi mevsimi tercih edersin?',
        'Sıcak mı soğuk mu seversin?',
        'Güneşli günlerde daha mı mutlu olursun?',
        'En sevdiğin hava durumu aktivitesi nedir?'
    ],

    'I love going to the beach': [
        'Denize gitmekten hoşlanırım.',
        'Deniz kenarında yapılan aktivitelerden hangisini seversin?',
        'En güzel plaj tatilini nerede yaptın?',
        'Deniz kenarında vakit geçirirken genellikle ne yaparsın?',
        'Deniz kenarında geçirdiğin en güzel anıyı paylaşabilir misin?'
    ],

    'whats your favorite way to exercise': [
        'Egzersiz yapmanın en sevdiğin yolu nedir?',
        'Hangi egzersiz aktivitelerini tercih edersin?',
        'Sporu günlük rutininin bir parçası yapar mısın?',
        'Egzersiz yaparken hangi müziği dinlersin?',
        'En sevdiğin sporcu veya spor takımı kimdir?'
    ],

    'whats your favorite type of cuisine': [
        'En sevdiğin mutfak türü nedir?',
        'Hangi ülkenin mutfağını tercih edersin?',
        'En sevdiğin mutfak kültürü nedir?',
        'Hangi lezzetleri en çok tercih edersin?',
        'Denemek istediğin bir mutfak tarifi var mı?'
    ],

    'Im a morning coffee person': [
        'Ben bir sabah kahve insanıyım.',
        'Günün hangi saatinde kahve içmeyi tercih edersin?',
        'Sabah kahvesinin senin için özel bir anlamı var mı?',
        'Kahve içerken genellikle ne yaparsın?',
        'Sabahları kahve içmek seni nasıl hissettirir?'
    ],



}

learnEnglish_b1 = {
'What is your favorite hobby': [
        'En sevdiğin hobi nedir?',
        'Genellikle boş zamanlarında nelerle ilgilenirsin?',
        'Hangi hobileri yapmayı tercih edersin?',
        'Hobilerin hakkında biraz konuşabilir misin?',
        'En çok hangi hobinle ilgileniyorsun?'
    ],
    'I enjoy hiking': [
        'Doğa yürüyüşlerinden keyif alırım.',
        'Yürüyüşe çıkmayı severim, özellikle doğada.',
        'Dağcılık benim için bir tutku haline geldi.',
        'Doğada vakit geçirmek beni rahatlatır.',
        'Güzel manzaralar görmekten hoşlanıyorum, özellikle yürüyüş sırasında.'
    ],
    'What is your favorite color': [
        'En sevdiğin renk nedir?',
        'Hangi renkleri genellikle tercih edersin?',
        'Renk seçimindeki tarzın nedir?',
        'Ev dekorasyonunda hangi renkleri kullanırsın?',
        'Renkler sana ne ifade eder?'
    ],
    'I love to travel to historical places': [
        'Tarihi yerlere seyahat etmeyi çok seviyorum.',
        'Antik şehirleri gezmek beni büyülüyor.',
        'Tarihi yerlere olan ilgim çok büyük.',
        'Geçmişe ait mekanları ziyaret etmek benim için önemli.',
        'Tarihi atmosferi hissetmek beni etkiler.'
    ],
    'I am interested in astronomy': [
        'Astronomiye ilgi duyarım.',
        'Yıldızları gözlemlemekten keyif alırım.',
        'Uzaya olan merakımı keşfetmeyi severim.',
        'Gece gökyüzünü izlemek beni büyüler.',
        'Uzayla ilgili kitapları okumayı severim.'
    ],
    'What is your favorite type of music': [
        'En sevdiğin müzik türü nedir?',
        'Hangi müzik türlerini genellikle dinlersin?',
        'Favori sanatçın kim?',
        'Konserlere gitmeyi sever misin?',
        'Müzikle ilgili favori anın nedir?'
    ],
    'I like to do yoga': [
        'Yoga yapmaktan hoşlanırım.',
        'Yoga benim için rahatlatıcıdır.',
        'Günlük yoga pratiği yaparım.',
        'Zihinsel sağlığıma katkı sağlar.',
        'Esneklik ve dengeyi artırmak için yoga yaparım.'
    ],
    'Do you enjoy cooking': [
        'Yemek yapmaktan hoşlanır mısın?',
        'Hangi yemekleri yapmayı seversin?',
        'Favori yemek tarifin nedir?',
        'Mutfakta zaman geçirmek seni mutlu eder mi?',
        'En son ne pişirdin?'
    ],
    'I like to play musical instruments': [
        'Müzik aleti çalmaktan hoşlanırım.',
        'Hangi enstrümanları çalmayı seversin?',
        'Müzik yeteneğin nedir?',
        'Kendi bestelerini yapar mısın?',
        'Müziğin sana nasıl bir etki yapıyor?'
    ],
    'What is your favorite holiday destination': [
        'En sevdiğin tatil yeri nedir?',
        'Hangi destinasyonları tercih edersin?',
        'Tatilde yapmayı sevdiğin şeyler nelerdir?',
        'Gezgin bir ruhun var mı?',
        'En güzel tatil anın nedir?'
    ],
  'I am currently learning a new language': [
        'Şu anda yeni bir dil öğreniyorum.',
        'Dil öğrenmek benim için önemli, şu sıralar bir dil çalışıyorum.',
        'Yeni bir dil öğrenmek zorlu olabilir, ama ben çaba sarf etmeyi seviyorum.',
        'Dil öğrenme sürecindeki zorluklarla baş etmeye çalışıyorum.',
        'Yeni bir dil öğrenmek, farklı kültürleri anlamamı sağlıyor.'
    ],
    'I like to attend cultural events': [
        'Kültürel etkinliklere katılmaktan hoşlanırım.',
        'Müzeleri ve galerileri gezmek beni heyecanlandırır.',
        'Tiyatro ve konserlere gitmeyi severim.',
        'Farklı kültürlerden gelen sanat eserlerini görmeyi seviyorum.',
        'Kültürel etkinlikler, benim için hem eğitici hem de keyifli olabilir.'
    ],
    'I enjoy outdoor activities': [
        'Dışarıda yapılan etkinliklerden keyif alırım.',
        'Doğada kamp yapmak ve piknikler düzenlemek benim için mükemmel bir zaman geçirme şekli.',
        'Spor etkinlikleri ve açık hava konserleri beni motive eder.',
        'Yürüyüş ve bisiklet turları yapmayı seviyorum.',
        'Her fırsatta dışarıda olmak, benim için stres atmanın harika bir yoludur.'
    ],
    'I am passionate about photography': [
        'Fotoğrafçılığa olan tutkum büyük.',
        'Fotoğraf çekmek, gördüğüm güzellikleri ve anıları ölümsüzleştirmeme olanak tanır.',
        'Çeşitli fotoğraf tekniklerini öğrenmeye çalışıyorum.',
        'Manzara ve portre fotoğrafçılığı benim favorimdir.',
        'Bazen sadece etrafı gözlemlemek ve güzel anları yakalamak için fotoğraf makinesini yanımda taşırım.'
    ],
    'I am planning to start a small business': [
        'Küçük bir işletme kurma planlarım var.',
        'Girişimcilik beni heyecanlandırıyor ve kendi işimi kurmak istiyorum.',
        'Hangi sektörde iş yapmak istediğime dair araştırmalar yapıyorum.',
        'İş planımı oluşturmak ve finansal stratejileri belirlemek için çalışıyorum.',
        'Kendi işimi kurmak, uzun vadeli bir hedefim ve hayalim.'
    ],
   'I like to explore different cuisines': [
        'Farklı mutfakları keşfetmeyi severim.',
        'Yemek denemek ve yeni lezzetleri tatmak benim için keyifli bir deneyimdir.',
        'Çeşitli restoranları ziyaret etmek, farklı kültürlerin mutfağını anlamama yardımcı oluyor.',
        'Evde yeni tarifler denemek ve yemek yapmak hoşuma gidiyor.',
        'Dünya mutfaklarından en sevdiğim yemekleri belirlemek için çaba sarf ediyorum.'
    ],
    'I am interested in technology trends': [
        'Teknoloji trendleriyle ilgilenirim.',
        'Yeni teknolojik gelişmeleri takip etmek benim için önemli.',
        'Yenilikçi ürünleri ve uygulamaları keşfetmeyi severim.',
        'Dijital dünyadaki değişiklikleri anlamak için çaba gösteriyorum.',
        'Teknolojinin günlük hayatımıza olan etkileri üzerine düşünmeyi severim.'
    ],
    'I enjoy attending live performances': [
        'Canlı performansları izlemekten keyif alırım.',
        'Konserlere, tiyatro oyunlarına ve dans gösterilerine gitmek benim için özel bir deneyimdir.',
        'Sanatçıların sahne enerjisi beni etkiler.',
        'Canlı performanslar, sanatın farklı ifadelerini deneyimlememe olanak tanır.',
        'Bir etkinlikte canlı performansın tadını çıkarmak, benim için unutulmaz bir anı oluşturur.'
    ],
    'I am passionate about environmental issues': [
        'Çevresel konulara tutkulu bir ilgim var.',
        'Sürdürülebilirlik ve çevre koruma konularında bilinçli hareket etmeye çalışıyorum.',
        'Atık azaltma ve geri dönüşüm konularında çaba sarf ediyorum.',
        'Doğa dostu uygulamaları benimsemek, benim için yaşam tarzı haline geldi.',
        'Çevresel sorunlarla ilgili farkındalık yaratmak ve insanları bilinçlendirmek için katkıda bulunmaya çalışıyorum.'
    ],
    'I like to participate in community events': [
        'Topluluk etkinliklerine katılmaktan hoşlanırım.',
        'Yerel topluluğuma katkı sağlamak için gönüllü çalışmalara katılırım.',
        'Topluluk etkinlikleri, insanlarla tanışmak ve bağlantı kurmak için harika bir fırsattır.',
        'Toplumda pozitif bir etki yaratmaya çalışarak kendimi daha iyi hissediyorum.',
        'Topluluk etkinliklerinin, dayanışma ve yardımlaşma duygusunu güçlendirdiğine inanıyorum.'
    ],
    'I am planning to pursue further education': [
        'Daha fazla eğitim almaya kararlıyım.',
        'Kariyerimde ilerlemek ve yeni beceriler kazanmak için eğitim planları yapıyorum.',
        'Öğrenmeye olan açık fikrim, sürekli gelişim ve kendini yenileme isteğim var.',
        'Yükseköğrenim veya sertifika programlarına katılmak için araştırmalar yapıyorum.',
        'Eğitim almak, kişisel ve profesyonel gelişimimde önemli bir rol oynar.'
    ],   'I like to explore different cuisines': [
        'Farklı mutfakları keşfetmeyi severim.',
        'Yemek denemek ve yeni lezzetleri tatmak benim için keyifli bir deneyimdir.',
        'Çeşitli restoranları ziyaret etmek, farklı kültürlerin mutfağını anlamama yardımcı oluyor.',
        'Evde yeni tarifler denemek ve yemek yapmak hoşuma gidiyor.',
        'Dünya mutfaklarından en sevdiğim yemekleri belirlemek için çaba sarf ediyorum.'
    ],
    'I am interested in technology trends': [
        'Teknoloji trendleriyle ilgilenirim.',
        'Yeni teknolojik gelişmeleri takip etmek benim için önemli.',
        'Yenilikçi ürünleri ve uygulamaları keşfetmeyi severim.',
        'Dijital dünyadaki değişiklikleri anlamak için çaba gösteriyorum.',
        'Teknolojinin günlük hayatımıza olan etkileri üzerine düşünmeyi severim.'
    ],
    'I enjoy attending live performances': [
        'Canlı performansları izlemekten keyif alırım.',
        'Konserlere, tiyatro oyunlarına ve dans gösterilerine gitmek benim için özel bir deneyimdir.',
        'Sanatçıların sahne enerjisi beni etkiler.',
        'Canlı performanslar, sanatın farklı ifadelerini deneyimlememe olanak tanır.',
        'Bir etkinlikte canlı performansın tadını çıkarmak, benim için unutulmaz bir anı oluşturur.'
    ],
    'I am passionate about environmental issues': [
        'Çevresel konulara tutkulu bir ilgim var.',
        'Sürdürülebilirlik ve çevre koruma konularında bilinçli hareket etmeye çalışıyorum.',
        'Atık azaltma ve geri dönüşüm konularında çaba sarf ediyorum.',
        'Doğa dostu uygulamaları benimsemek, benim için yaşam tarzı haline geldi.',
        'Çevresel sorunlarla ilgili farkındalık yaratmak ve insanları bilinçlendirmek için katkıda bulunmaya çalışıyorum.'
    ],
    'I like to participate in community events': [
        'Topluluk etkinliklerine katılmaktan hoşlanırım.',
        'Yerel topluluğuma katkı sağlamak için gönüllü çalışmalara katılırım.',
        'Topluluk etkinlikleri, insanlarla tanışmak ve bağlantı kurmak için harika bir fırsattır.',
        'Toplumda pozitif bir etki yaratmaya çalışarak kendimi daha iyi hissediyorum.',
        'Topluluk etkinliklerinin, dayanışma ve yardımlaşma duygusunu güçlendirdiğine inanıyorum.'
    ],
    'I am planning to pursue further education': [
        'Daha fazla eğitim almaya kararlıyım.',
        'Kariyerimde ilerlemek ve yeni beceriler kazanmak için eğitim planları yapıyorum.',
        'Öğrenmeye olan açık fikrim, sürekli gelişim ve kendini yenileme isteğim var.',
        'Yükseköğrenim veya sertifika programlarına katılmak için araştırmalar yapıyorum.',
        'Eğitim almak, kişisel ve profesyonel gelişimimde önemli bir rol oynar.'
    ],   'I like to explore different cuisines': [
        'Farklı mutfakları keşfetmeyi severim.',
        'Yemek denemek ve yeni lezzetleri tatmak benim için keyifli bir deneyimdir.',
        'Çeşitli restoranları ziyaret etmek, farklı kültürlerin mutfağını anlamama yardımcı oluyor.',
        'Evde yeni tarifler denemek ve yemek yapmak hoşuma gidiyor.',
        'Dünya mutfaklarından en sevdiğim yemekleri belirlemek için çaba sarf ediyorum.'
    ],
    'I am interested in technology trends': [
        'Teknoloji trendleriyle ilgilenirim.',
        'Yeni teknolojik gelişmeleri takip etmek benim için önemli.',
        'Yenilikçi ürünleri ve uygulamaları keşfetmeyi severim.',
        'Dijital dünyadaki değişiklikleri anlamak için çaba gösteriyorum.',
        'Teknolojinin günlük hayatımıza olan etkileri üzerine düşünmeyi severim.'
    ],
    'I enjoy attending live performances': [
        'Canlı performansları izlemekten keyif alırım.',
        'Konserlere, tiyatro oyunlarına ve dans gösterilerine gitmek benim için özel bir deneyimdir.',
        'Sanatçıların sahne enerjisi beni etkiler.',
        'Canlı performanslar, sanatın farklı ifadelerini deneyimlememe olanak tanır.',
        'Bir etkinlikte canlı performansın tadını çıkarmak, benim için unutulmaz bir anı oluşturur.'
    ],
    'I am passionate about environmental issues': [
        'Çevresel konulara tutkulu bir ilgim var.',
        'Sürdürülebilirlik ve çevre koruma konularında bilinçli hareket etmeye çalışıyorum.',
        'Atık azaltma ve geri dönüşüm konularında çaba sarf ediyorum.',
        'Doğa dostu uygulamaları benimsemek, benim için yaşam tarzı haline geldi.',
        'Çevresel sorunlarla ilgili farkındalık yaratmak ve insanları bilinçlendirmek için katkıda bulunmaya çalışıyorum.'
    ],
    'I like to participate in community events': [
        'Topluluk etkinliklerine katılmaktan hoşlanırım.',
        'Yerel topluluğuma katkı sağlamak için gönüllü çalışmalara katılırım.',
        'Topluluk etkinlikleri, insanlarla tanışmak ve bağlantı kurmak için harika bir fırsattır.',
        'Toplumda pozitif bir etki yaratmaya çalışarak kendimi daha iyi hissediyorum.',
        'Topluluk etkinliklerinin, dayanışma ve yardımlaşma duygusunu güçlendirdiğine inanıyorum.'
    ],
    'I am planning to pursue further education': [
        'Daha fazla eğitim almaya kararlıyım.',
        'Kariyerimde ilerlemek ve yeni beceriler kazanmak için eğitim planları yapıyorum.',
        'Öğrenmeye olan açık fikrim, sürekli gelişim ve kendini yenileme isteğim var.',
        'Yükseköğrenim veya sertifika programlarına katılmak için araştırmalar yapıyorum.',
        'Eğitim almak, kişisel ve profesyonel gelişimimde önemli bir rol oynar.'
    ], 'I often collaborate with colleagues on projects': [
        'Projelerde sıkça meslektaşlarımla işbirliği yaparım.',
        'Takım çalışması benim için önemlidir, projelerde birlikte çalışmayı severim.',
        'Farklı bakış açılarını bir araya getirerek daha etkili çözümler bulabiliriz.',
        'İşbirliği içinde çalışmak, hem kişisel hem de profesyonel gelişimime katkı sağlar.',
        'Birlikte çalıştığımızda, herkesin güçlü yönlerini kullanarak daha başarılı olabiliriz.'
    ],
    'I enjoy reading about current affairs': [
        'Güncel konuları okumaktan keyif alırım.',
        'Haberleri ve güncel olayları takip etmek, dünyada neler olup bittiğini anlamama yardımcı olur.',
        'Farklı haber kaynaklarından bilgi alarak, olayları farklı perspektiflerden değerlendirmeye çalışırım.',
        'Toplumda gerçekleşen değişimleri anlamak ve etkileşimde bulunmak benim için önemlidir.',
        'Güncel konular hakkında bilgi sahibi olmak, bilinçli bir vatandaş olmama katkı sağlar.'
    ],
    'I like to stay physically active': [
        'Fiziksel olarak aktif kalmaktan hoşlanırım.',
        'Spor yapmak, hem bedensel hem zihinsel sağlığım için önemlidir.',
        'Farklı sporları denemek ve egzersiz rutinimi çeşitlendirmek benim için keyiflidir.',
        'Her gün kısa bir yürüyüş yapmak veya egzersiz yapmak, enerji seviyemi yükseltir.',
        'Aktif bir yaşam tarzı sürdürmek, genel sağlığımı korumama yardımcı olur.'
    ],
    'I often socialize with friends and family': [
        'Sıkça arkadaşlarım ve ailemle sosyalleşirim.',
        'Sosyal bağlantılarımı güçlendirmek ve ilişkilerimi sürdürmek benim için önemlidir.',
        'Arkadaşlarımla buluşmak, hem eğlenceli zaman geçirmeme hem de destek sistemimi güçlendirmeme yardımcı olur.',
        'Ailemle düzenli olarak vakit geçirmek, duygusal bağlarımı güçlendirir.',
        'Sosyal etkileşim, hayatımın önemli bir parçasıdır ve beni mutlu eder.'
    ],
    'I am passionate about helping others': [
        'Diğer insanlara yardım etmeye tutkulu biriyim.',
        'Gönüllü çalışmalara katılarak topluma katkıda bulunmayı severim.',
        'Başkalarına yardım etmek, hem topluluğumuzun hem de bireylerin daha iyi bir yerde olmasına yardımcı olabilir.',
        'Empati kurmak ve başkalarının ihtiyaçlarına duyarlı olmak, benim için değerli değerlerdir.',
        'Küçük bir yardımın bile büyük bir fark yaratabileceğine inanıyorum.'
    ],
    'I am interested in learning about different cultures': [
        'Farklı kültürleri öğrenmeye ilgiliyim.',
        'Yabancı kültürleri anlamak, dünya görüşümü genişletmeme ve hoşgörülü bir birey olmama yardımcı olur.',
        'Yabancı dilleri öğrenmek ve diğer kültürlerin geleneklerini keşfetmek benim için heyecan verici bir deneyimdir.',
        'Farklı kültürlerle etkileşimde bulunmak, önyargıları azaltabilir ve kültürel çeşitliliği kutlayabilir.',
        'Seyahat etmek ve yeni yerler keşfetmek, benim için öğrenme ve keşfetme arzusunu tatmin eder.'
    ],

}
learnEnglish_b2 = {
     'I enjoy exploring new hobbies and activities': [
        'Yeni hobiler ve aktiviteler keşfetmeyi seviyorum.',
        'Farklı hobilere zaman ayırmak, rutinimi renklendirmeme ve kendimi geliştirmeme yardımcı olur.',
        'Yaratıcı faaliyetlere katılmak, zihinsel sağlığımı destekler ve stresle başa çıkmama yardımcı olur.',
        'Farklı sporları denemek, hem fiziksel hem de zihinsel olarak aktif kalmamı sağlar.',
        'Yeni şeyler öğrenmek, benim için bir yaşam tarzı haline gelmiştir.'
    ],

    'I believe in the importance of maintaining a healthy work-life balance': [
        'Sağlıklı bir iş-yaşam dengesinin önemine inanıyorum.',
        'İş ve özel hayat arasında denge kurmak, hem kariyerimde başarılı olmama hem de kişisel refahımı korumama yardımcı olur.',
        'Zaman yönetimi becerilerimi geliştirmek, iş stresiyle daha iyi başa çıkmama katkı sağlar.',
        'Dinlenmeye ve rekreasyona zaman ayırmak, enerjimi yenilememi sağlar ve iş verimimi artırır.',
        'Kaliteli zaman geçirmek, hem iş hem de sosyal yaşantımda mutluluğumu artırır.'
    ],

    'I find joy in exploring nature and the outdoors': [
        'Doğayı ve açık havayı keşfetmekten keyif alıyorum.',
        'Yürüyüşe çıkmak ve doğal güzellikleri gözlemlemek, ruhsal huzurumu artırır.',
        'Açık havada spor yapmak, hem fiziksel formumu korumama hem de doğayla iç içe olmama yardımcı olur.',
        'Piknik yapmak ve doğal alanlarda vakit geçirmek, stresi azaltır ve pozitif enerji sağlar.',
        'Çeşitli doğa aktiviteleri, benim için dinlendirici ve keyifli bir kaçış sunar.'
    ],

    'I value continuous learning and personal development': [
        'Sürekli öğrenmeyi ve kişisel gelişimi önemsiyorum.',
        'Kitap okuma, online kurslara katılma ve yeni beceriler edinme, kendimi geliştirmemde önemli bir rol oynar.',
        'Kariyer hedeflerime ulaşmak için sürekli olarak bilgi ve yeteneklerimi artırmaya çalışıyorum.',
        'Mevcut bilgilerimi güncel tutmak, değişen dünyaya ayak uydurmama yardımcı olur.',
        'Her gün bir şeyler öğrenmek, benim için yaşamın anlamını artırır.'
    ],

    'I believe in the power of positive thinking': [
        'Pozitif düşünmenin gücüne inanıyorum.',
        'Olumlu düşünce tarzı, zorluklarla başa çıkmamı kolaylaştırır ve genel yaşam kalitemi artırır.',
        'Olumlu bir bakış açısıyla yaklaşmak, çevremdeki insanlar üzerinde olumlu bir etki yaratır.',
        'Teşekkür etmek ve minnettarlık duygularını sıkça ifade etmek, ruhsal sağlığımı güçlendirir.',
        'Olumlu enerjiyi yaymak, etrafımdaki ilişkileri olumlu yönde etkiler ve güçlendirir.'
    ],

    'I enjoy working collaboratively with others':[
     'Diğerleriyle işbirliği yapmaktan keyif alıyorum.'
     'Takım çalışmaları, farklı bakış açılarını bir araya getirerek daha yaratıcı çözümler bulmama yardımcı olur.'
     'İş arkadaşlarımla düzenli olarak fikir alışverişi yapmak, profesyonel gelişimime katkı sağlar.'
     'Proje gruplarında yer almak, sorumluluk paylaşımı ve işbirliği becerilerimi güçlendirir.'
     'Ortak projelerde yer almak, ekip ruhunu oluşturarak başarıya ulaşmayı destekler.'
    ],

    'I am passionate about promoting diversity and inclusion':[
    'Çeşitliliği ve dahil ediciliği teşvik etmek konusunda tutkulu biriyim.'
    'Çeşitli perspektifleri anlamak, iş ortamında daha zengin bir kültür oluşturmama yardımcı olur.'
    'Eşitlik ve adaleti desteklemek, toplumsal değişime katkı sağlamama yardımcı olabilir.'
    'Çeşitli eğitim programlarına katılmak, farkındalığımı artırarak daha etkili bir lider olmama yardımcı olur.'
     'İş yerinde herkesin duyulduğunu hissettiği bir ortamın oluşturulması, iş performansını artırır.'],

    'I enjoy learning about new technologies':[
     'Yeni teknolojiler hakkında bilgi edinmekten keyif alıyorum.'
     'Gelişen dijital dünyayı takip etmek, iş süreçlerini optimize etme becerilerimi artırır.'
     'Teknolojik yeniliklere adapte olmak, rekabet avantajı elde etmeme yardımcı olur.'
     'Online teknoloji forumlarına katılmak, sektördeki en son gelişmeleri öğrenmeme yardımcı olur.'
     'Yeni uygulamalar ve yazılımlar keşfetmek, iş verimliliğimi artırır.'],

    'I believe in fostering a positive work environment':[
     'Pozitif bir çalışma ortamını desteklemenin önemine inanıyorum.'
     'İş arkadaşlarına destek olmak, ekip morale olumlu bir etki yapar.'
     'Takım içinde iletişimi güçlendirmek, projelerin daha verimli bir şekilde ilerlemesine katkı sağlar.'
     'Çalışanların geri bildirimlerini dikkate almak, şirket kültürünü iyileştirmeme yardımcı olur.'
     'Çalışma arkadaşları arasında dayanışmayı teşvik etmek, iş tatminini artırır.'],

    'I enjoy participating in community service activities':[
     'Toplum hizmeti etkinliklerine katılmaktan keyif alıyorum.'
     'Gönüllü projelere dahil olmak, sosyal sorumluluk duygumu güçlendirir.'
     'Topluluk yardımı etkinliklerine katılmak, çevremdeki insanlara yardım etmenin memnuniyetini yaşamama yardımcı olur.'
     'Sosyal projelerde yer almak, toplumda olumlu değişikliklere katkı sağlamama yardımcı olur.'
     'Gönüllü çalışmalara katılmak, kişisel büyüme ve empati geliştirmeme olanak tanır.'],

    'I value effective communication skills':[
     'Etkili iletişim becerilerini önemsiyorum.'
     'Açık ve net iletişim, iş süreçlerini düzenlememe ve sorunları daha hızlı çözmeme yardımcı olur.'
     'İş arkadaşlarıyla etkili iletişim kurmak, projelerin daha koordineli bir şekilde ilerlemesine katkı sağlar.'
     'Sunum becerilerimi geliştirmek, fikirleri etkili bir şekilde aktarmama yardımcı olur.'
     'Empati becerilerini kullanarak, ekip içinde daha iyi bir iletişim kurabilirim.'
    ],

    'I am interested in exploring different cuisines':[
     'Farklı mutfakları keşfetmeye ilgiliyim.'
     'Yerel yemek festivallerine katılmak, dünya çapındaki lezzetleri deneyimleme şansı tanır.'
     'Farklı kültürlerin yemek alışkanlıklarını incelemek, kültürel çeşitliliği anlamama yardımcı olur.'
     'Evde yeni tarifler denemek, yaratıcı yemekler yapmama olanak sağlar.'
     'Dünya mutfaklarından öğrenilenleri kendi yemeklerime uyarlamak, kişisel becerilerimi artırır.'
    ],

    'I believe in setting achievable goals':[
     'Ulaşılabilir hedefler belirlemenin önemine inanıyorum.'
     'Kısa vadeli ve uzun vadeli hedefler, motivasyonumu artırarak başarıya ulaşmama yardımcı olur.'
     'Hedeflere ulaşmak için plan yapmak, organizasyon becerilerimi güçlendirir.'
     'İlerleme kaydedilen hedefleri kutlamak, motivasyonu yüksek tutmama yardımcı olur.'
     'Hedeflerime adım adım ilerlemek, kişisel başarılarımı artırır.'
    ],

    'I enjoy attending live performances':[
     'Canlı performanslara katılmaktan keyif alıyorum.'
     'Tiyatro oyunları ve konserlere gitmek, sanatsal deneyimleri yaşamama olanak tanır.'
     'Sahne sanatlarına olan ilgim, kültürel etkinliklere katılımımı artırır.'
     'Canlı performansları izlemek, sanatçıların özgün yeteneklerini takdir etmeme yardımcı olur.'
     'Farklı türlerdeki performansları deneyimlemek, sanat dünyasındaki çeşitliliği keşfetmeme yardımcı olur.'
    ],

    'I value time management skills':[
     'Zaman yönetimi becerilerini önemsiyorum.'
     'İş görevlerimi düzenli olarak planlamak, verimliliğimi artırır.'
     'Öncelikli görevleri belirlemek, iş performansımı optimize etmeme yardımcı olur.'
     'Zamanı etkili bir şekilde kullanmak, kişisel ve profesyonel yaşam dengesini sürdürmeme yardımcı olur.'
     'Zaman yönetimi becerilerimi geliştirmek, stresle daha etkili bir şekilde başa çıkmama yardımcı olur.'
    ],

}