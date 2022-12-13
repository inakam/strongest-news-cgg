from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)

def test_root_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}

def test_all_comments():
    response = client.get("/comments")
    assert response.status_code == 200
    assert response.json() == [{"article_id":0,"created_at":"2020-07-21T20:00:00","name":"田中太郎","detail":"感動しました！","id":1,"updated_at":"2020-07-21T20:00:00"},{"article_id":1,"created_at":"2022-02-28T21:00:00","name":"田中正志","detail":"いいニュースですね！","id":2,"updated_at":"2022-02-28T21:00:00"}]

def test_comment_0():
    response = client.get("/comments/0")
    assert response.status_code == 200
    assert response.json() == [{"article_id":0,"created_at":"2020-07-21T20:00:00","detail":"感動しました！","id":1,"name":"田中太郎","updated_at":"2020-07-21T20:00:00"}]

def test_article_0():
    response = client.get("/articles/0")
    assert response.status_code == 200
    assert response.json() == {
        "created_at": "2022-04-02T08:30:00",
        "id": 0,
        "detail": "<p>女優の松井愛莉さんが、人生初のカレンダー発売記念イベントを行いました。</p><br><img src=\"https://s.mxtv.jp/tokyomxplus/mx/public/article/mainVisual/1jo1wnwx8froj93i75zhezrf4325ww.jpg\" width=\"90%\" class=\"img_contents\"><br><p>松井さんは、「千葉のいろんな所で撮ったんですけど、日本なのかな？と思うぐらい、キレイな写真をたくさん撮っていただきました」と撮影エピソードを披露。</p><p>記者から「千葉のどちらで撮られたんですか？」と聞かれた松井さんは、</p><p>「千葉の&hellip;えー、端っこの方です」と笑いながら答えました。</p><p>松井さんは去年の秋からショートカットにしたそうで、その理由を聞いてみると？</p><p>「私がただ単に（髪を）切りたくて、頑張ってマネージャーさんを説得して&hellip;」</p><p>「切りました、ハイ！」を笑顔を見せました。</p><p>さらに「マネージャーさんはずっと許してくれなかったので、もうメチャメチャ切りたい！という思いを必死に伝えてOK貰いました」と振り返りました。</p>",
        "img_url": "https://s.mxtv.jp/tokyomxplus/mx/public/article/mainVisual/1jo1wnwx8froj93i75zhezrf4325ww.jpg",
        "updated_at": "2022-04-02T08:30:00",
        "title": "松井愛莉、念願のショートカットに！",
        "type": "エンタメ"
    }

def test_article_limit1():
    response = client.get("/articles?limit=1")
    assert response.status_code == 200
    assert response.json() == [{"title":"自閉症への理解深めて　大阪城を青色ライトアップ　世界啓発デー","type":"社会","detail":"<p>「世界自閉症啓発デー」の2日、大阪市中央区の大阪城など全国各地の名所などがシンボルカラーの青色にライトアップされた。「癒やし」や「希望」の意味が込められているという。</p><p>啓発デーは2007年、自閉症など発達障害への理解を深めてもらおうと国連が定めた。大阪城では桜が見ごろを迎える中、たくさんの人が青色に照らされた天守閣の姿をカメラに収めていた。そのほか、「太陽の塔」（大阪府吹田市）や姫路城（兵庫県姫路市）など全国約250カ所がライトアップされた。【隈元悠太】</p>","created_at":"2022-04-02T11:39:21","img_url":"https://cdn.mainichi.jp/vol1/2022/04/02/20220402k0000m040218000p/9.jpg","id":376,"updated_at":"2022-04-02T11:39:21"}]

def test_article_limit3():
    response = client.get("/articles?limit=3")
    assert response.status_code == 200
    assert response.json() == [{"title":"自閉症への理解深めて　大阪城を青色ライトアップ　世界啓発デー","type":"社会","detail":"<p>「世界自閉症啓発デー」の2日、大阪市中央区の大阪城など全国各地の名所などがシンボルカラーの青色にライトアップされた。「癒やし」や「希望」の意味が込められているという。</p><p>啓発デーは2007年、自閉症など発達障害への理解を深めてもらおうと国連が定めた。大阪城では桜が見ごろを迎える中、たくさんの人が青色に照らされた天守閣の姿をカメラに収めていた。そのほか、「太陽の塔」（大阪府吹田市）や姫路城（兵庫県姫路市）など全国約250カ所がライトアップされた。【隈元悠太】</p>","created_at":"2022-04-02T11:39:21","img_url":"https://cdn.mainichi.jp/vol1/2022/04/02/20220402k0000m040218000p/9.jpg","id":376,"updated_at":"2022-04-02T11:39:21"},{"title":"“新成人”張本智和、早稲田大入学「今まで以上に自覚を持って頑張っていきます」茶髪写真も投稿","type":"卓球","detail":"<p>卓球日本代表で東京五輪団体銅メダリストの張本智和が自身のTwitterを更新し、「早稲田大学人間科学部（通信教育課程）に入学しました！」と大学進学を報告した。</p><h2>張本は早稲田大学へ</h2><p>張本は自身のTwitterで「早稲田大学人間科学部（通信教育課程）に入学しました！4月から成人になり、そして大学生にもなりました」とツイート。日本大学高等学校を3月に卒業し、4月からは早稲田大学人間科学部（通信教育課程）に進み、引き続きプロ卓球選手として活動を続ける。</p><p>また、成人年齢引き下げにより、18歳の張本はこのタイミングで新成人となり、また大学進学を機に新たな決意を表明した。「今まで以上に自覚を持って頑張っていきます。これからもよろしくお願いします！」。</p><p>茶髪に染めた髪色で笑顔のスーツ姿で写った張本の写真もツイートには添付されており、大学生活への期待に胸を膨らませる張本の様子が見てとれる。</p><p>第1回パリ五輪選考となったLION CUP TOP32で優勝し、今後も日本卓球界を牽引していくであろう張本に対し、ファンからも「学業に卓球に益々のご活躍を！」「スーツ似合ってますね！かっこいい」「大学入学おめでとうございます」と祝福のコメントが相次いでいる。</p><p></p><p></p><p>文：ラリーズ編集部</p>","created_at":"2022-04-02T11:23:05","img_url":"http://rallys.online/wp-content/uploads/2022/03/3J2A3502-1-330x186.jpg","id":287,"updated_at":"2022-04-02T11:23:05"},{"title":"ハロプロ「ひなフェス」開催　卒業発表のモー娘・森戸知沙希、Juice＝Juice・稲場愛香が心境を明かす","type":"エンタメ","detail":"ハロー！プロジェクトのグループが一同に会する春の恒例コンサート「Hello! Project ひなフェス 2022」が2日、千葉・幕張メッセ 国際展示場で開催。2日間で4公演行う初回公演後に各グループの代表メンバーが囲み取材に出席した。<br /><br />会見に参加したのは、モーニング娘。’22・譜久村聖と森戸知沙希、アンジュルム・平山遊季、Juice＝Juice・稲場愛香と江端妃咲、つばきファクトリー・岸本ゆめの、BEYOOOOONDS・山崎夢羽、OCHA NORMA・米村姫良々の8名。<br /><br />さらに、本公演でつんくの書き下ろし楽曲「Hello! 生まれた意味がきっとある」をOCHA NORMAとコラボレーションした人気キャラクターのハローキティも登場した。<br /><br />恒例の「ひなフェス」について、モーニング娘。’22とハロプロのリーダーを務める譜久村は「ひな祭りとしてみんなでお祭り騒ぎできるのが、すごく楽しい」とコメント。「今回みたいにキティちゃんが来てくれたりとか、毎年特別なことが何かあるんですよ。それが私たちにとってすごく楽しくて。毎年この時間が楽しみ」と喜んだ。<br /><br />ハロプロ研修生から昇格後、アンジュルム新メンバーとして初めて「ひなフェス」に参加した平山は「研修生でいるときも出させていただいんですけど、アンジュルムになってから出させていただいて、より場位置（ステージ上の立ち位置）が複雑だったり、出させていただく曲が多くなった」とコメント。「緊張感もありながら、たくさんの先輩に支えていただいたりして、すごく楽しむことができています」と語った。<br /><br />5月30日の日本武道館公演でのグループとハロプロ卒業を発表しているJuice＝Juiceの稲場は、自身最後となる「ひなフェス」について「毎年覚えることがたくさんあるんですね。大きい会場で場位置を覚えるのもかなり大変なんですけど、そのぶんメンバーの絆も深まって、達成感も大きい」と話すと、ポーズを決めて「ひなフェス、がんばります！」と元気よく宣言。<br /><br />稲場と同じく、6月20日の日本武道館公演でモー娘。とハロプロを卒業する森戸は「『ああ、終わっちゃうんだ。終わらないでほしいな』という、今の気持ちです」と寂しさをにじませた。<br /><br />本公演は2日間にわたり、モーニング娘。’22、アンジュルム、Juice＝Juice、つばきファクトリー＆BEYOOOOONDSがメインアクトの4公演を開催。グループによるパフォーマンスだけでなく、事前に行われた抽選会によって選ばれたメンバーによる、 ソロや当日限りのシャッフルユニットによるパフォーマンスも披露する。","created_at":"2022-04-02T11:22:00","img_url":"https://www.crank-in.net/img/db/229046021202027_300.jpg","id":44,"updated_at":"2022-04-02T11:22:00"}]

def test_article_13():
    response = client.get("/articles/13")
    assert response.status_code == 200
    assert response.json() == {
        "created_at": "2022-03-27T12:30:00",
        "id": 13,
        "detail": "<p>東京リベンジャーズとポイントカードがコラボした「T番隊」結成＆隊長就任式イベントが行われ、マイキーこと佐野万次郎役の声優・林勇さんと、タレントのDAIGOさんが出席しました。</p><br><img src=\"https://s.mxtv.jp/tokyomxplus/mx/public/article/mainVisual/sr6njx2w76xws4hzl089sia07c26d5.jpg\" width=\"90%\" class=\"img_contents\"><br><p>林さんは「T番隊入るの日和っているやついる？いねえよな！」とマイキーの名台詞を披露しました。</p><p>そして「T番隊 隊長は DAIGO！覚えておけ！」とDAIGOさんを紹介。</p><p>DAIGOさんは「T番隊 隊長に就任することになりました。よろしくお願いしまーす！」と挨拶しました。</p><p>隊長に就任したDAIGOさんは、特攻服をプレゼントされました。</p><p>今の感想を聞かれたDAIGOさんは、「気持ちですか&hellip;T ですね。楽しい」とDAI語で表現していました。</p>",
        "img_url": "https://s.mxtv.jp/tokyomxplus/mx/public/article/mainVisual/sr6njx2w76xws4hzl089sia07c26d5.jpg",
        "updated_at": "2022-03-27T12:30:00",
        "title": "DAIGO、東京卍會の隊長就任をDAI語で表現！",
        "type": "エンタメ"
    }

def test_titles_limit9():
    response = client.get("/titles?limit=9")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 376,
            "title": "自閉症への理解深めて　大阪城を青色ライトアップ　世界啓発デー",
            "img_url": "https://cdn.mainichi.jp/vol1/2022/04/02/20220402k0000m040218000p/9.jpg",
            "created_at": "2022-04-02T11:39:21"
        },
        {
            "id": 287,
            "title": "“新成人”張本智和、早稲田大入学「今まで以上に自覚を持って頑張っていきます」茶髪写真も投稿",
            "img_url": "http://rallys.online/wp-content/uploads/2022/03/3J2A3502-1-330x186.jpg",
            "created_at": "2022-04-02T11:23:05"
        },
        {
            "id": 44,
            "title": "ハロプロ「ひなフェス」開催　卒業発表のモー娘・森戸知沙希、Juice＝Juice・稲場愛香が心境を明かす",
            "img_url": "https://www.crank-in.net/img/db/229046021202027_300.jpg",
            "created_at": "2022-04-02T11:22:00"
        },
        {
            "id": 374,
            "title": "「さらなる被害実態の掘り起こしの必要性ある」　カネミ油症次世代調査",
            "img_url": "https://cdn.mainichi.jp/vol1/2022/04/02/20220402k0000m040188000p/9.jpg",
            "created_at": "2022-04-02T11:16:38"
        },
        {
            "id": 45,
            "title": "アンジャッシュ児嶋、『王様のブランチ』新リポーターに「スキャンダルだけは気を付けて」",
            "img_url": "https://www.crank-in.net/img/db/224045023200044_300.jpg",
            "created_at": "2022-04-02T11:15:00"
        },
        {
            "id": 378,
            "title": "ナイナイ岡村隆史さん、第1子誕生を公表　大阪の舞台で",
            "img_url": "https://cdn.mainichi.jp/vol1/2022/04/02/20220402k0000m200191000p/9.jpg",
            "created_at": "2022-04-02T11:02:40"
        },
        {
            "id": 50,
            "title": "『4人はそれぞれウソをつく』TVアニメ化　秘密だらけの曲者4人のカオス学園コメディ",
            "img_url": "https://www.crank-in.net/img/db/226049026162211_300.jpg",
            "created_at": "2022-04-02T11:00:00"
        },
        {
            "id": 46,
            "title": "華原朋美、ダイエットの成果をインスタグラムで公開",
            "img_url": "https://www.crank-in.net/img/db/218105029156489_300.jpg",
            "created_at": "2022-04-02T11:00:00"
        },
        {
            "id": 289,
            "title": "【Tリーグ】松平健太、T.T彩たまと契約更新「今シーズンはもう優勝しかない」",
            "img_url": "http://rallys.online/wp-content/uploads/2022/02/cut-10-330x186.jpg",
            "created_at": "2022-04-02T10:56:03"
        }
    ]

def test_titles_limit3():
    response = client.get("/titles?limit=3")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 376,
            "title": "自閉症への理解深めて　大阪城を青色ライトアップ　世界啓発デー",
            "img_url": "https://cdn.mainichi.jp/vol1/2022/04/02/20220402k0000m040218000p/9.jpg",
            "created_at": "2022-04-02T11:39:21"
        },
        {
            "id": 287,
            "title": "“新成人”張本智和、早稲田大入学「今まで以上に自覚を持って頑張っていきます」茶髪写真も投稿",
            "img_url": "http://rallys.online/wp-content/uploads/2022/03/3J2A3502-1-330x186.jpg",
            "created_at": "2022-04-02T11:23:05"
        },
        {
            "id": 44,
            "title": "ハロプロ「ひなフェス」開催　卒業発表のモー娘・森戸知沙希、Juice＝Juice・稲場愛香が心境を明かす",
            "img_url": "https://www.crank-in.net/img/db/229046021202027_300.jpg",
            "created_at": "2022-04-02T11:22:00"
        }
    ]

def test_keyword_nogizaka46():
    response = client.get("/keywords?keyword=%E4%B9%83%E6%9C%A8%E5%9D%82")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 144,
            "title": "「乃木坂46」に5期生が新加入！ データから見る“シングル選抜メンバー”に入る確率",
            "img_url": "https://jprime.ismcdn.jp/mwimgs/2/0/620/img_200f83d54330e724ec277cfb77d22f61452374.jpg",
            "created_at": "2022-04-01T20:00:00"
        },
        {
            "id": 317,
            "title": "『乃木坂46』現役メンバーが過激演技!?「怖くて見れない」 とファン大混乱",
            "img_url": "https://myjitsu.jp/wp-content/uploads/2022/04/shutterstock_1472754191-1.jpg",
            "created_at": "2022-04-02T02:02:35"
        },
        {
            "id": 319,
            "title": "『乃木坂46』不買運動でオワコンへ…新曲CDの売上が激減！ 今週の嫌われ女ランキング",
            "img_url": "https://myjitsu.jp/wp-content/uploads/2021/09/nogizaka1.jpg",
            "created_at": "2022-04-02T02:00:31"
        },
        {
            "id": 342,
            "title": "『乃木坂46』に吹き荒れる逆風…クラスター発生はライブ打ち上げが原因？",
            "img_url": "https://myjitsu.jp/wp-content/uploads/2021/09/nogizaka1.jpg",
            "created_at": "2022-04-01T02:04:29"
        }
    ]

def test_keyword_will():
    response = client.get("/keywords?keyword=%E3%82%A6%E3%82%A3%E3%83%AB%E3%83%BB%E3%82%B9%E3%83%9F%E3%82%B9")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 76,
            "title": "ウィル・スミスがクリス・ロックに強烈ビンタ!! 二人は共演者であり長年の友人同士!? アカデミー賞授賞式から一夜明けてスミスが謝罪文を公開",
            "img_url": "https://www.banger.jp/wp-content/uploads/2022/03/shutterstock_347498957-300x200.jpg",
            "created_at": "2022-03-29T08:02:00"
        },
        {
            "id": 310,
            "title": "ウィル・スミスの“ビンタ事件”だけじゃない！ アカデミー賞で起こった珍事",
            "img_url": "https://myjitsu.jp/wp-content/uploads/2022/04/will-smith1.jpg",
            "created_at": "2022-04-02T08:34:27"
        },
        {
            "id": 347,
            "title": "ウィル・スミスの“暴行事件”擁護しているのは女性・低所得・低学歴と判明",
            "img_url": "https://myjitsu.jp/wp-content/uploads/2022/04/will-smith1.jpg",
            "created_at": "2022-04-01T01:33:34"
        },
        {
            "id": 391,
            "title": "ウィル・スミスさん、アカデミー会員辞任　平手打ち「信頼裏切った」",
            "img_url": "https://cdn.mainichi.jp/vol1/2022/04/02/20220402k0000m200042000p/9.jpg",
            "created_at": "2022-04-02T01:01:07"
        }
    ]

def test_categories_newnews():
    response = client.get("/categories?type=%E6%96%B0%E7%9D%80%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 66,
            "title": "【やっぱりU-NEXTを選ぶワケ】見放題本数ダントツNo.1、雑誌も読み放題！お得なポイントの使い道は？サービスを徹底解剖!!",
            "img_url": "https://www.banger.jp/wp-content/uploads/2022/03/ogp.d665117514a37a0e913dc753f06ba5f0-300x158.png",
            "created_at": "2022-03-31T10:46:51"
        },
        {
            "id": 67,
            "title": "ブルース・ウィリスが失語症のため俳優を引退　スタローン、トラボルタなど映画界の著名人による称賛の声や温かいメッセージ",
            "img_url": "https://www.banger.jp/wp-content/uploads/2022/04/shutterstock_317285057_bw-300x200.jpg",
            "created_at": "2022-04-01T08:17:28"
        },
        {
            "id": 69,
            "title": "Netflixが2022年4月配信開始の最新コンテンツを発表！劇場公開に先行しNetflixで独占配信『バブル』や男性妊娠を描く「ヒヤマケンタロウの妊娠」など話題作の数々を見逃すな!!",
            "img_url": "https://www.banger.jp/wp-content/uploads/2022/03/01_Bubble_main_1st-300x212.jpg",
            "created_at": "2022-03-31T09:18:11"
        },
        {
            "id": 71,
            "title": "【全受賞結果!!】第94回アカデミー賞 国際長編映画賞は『ドライブ・マイ・カー』作品賞は『コーダ あいのうた』",
            "img_url": "https://www.banger.jp/wp-content/uploads/2021/07/sub5-300x200.jpg",
            "created_at": "2022-03-28T04:35:45"
        },
        {
            "id": 72,
            "title": "HBO Max、『IT／イット』の殺人鬼“ペニーワイズ”を主人公にした前日譚ドラマを製作！ ペニーワイズのドキュメンタリー映画の全米公開も決定!!",
            "img_url": "https://www.banger.jp/wp-content/uploads/2022/03/maxresdefault-1-3-300x169.jpeg",
            "created_at": "2022-03-30T09:09:22"
        },
        {
            "id": 74,
            "title": "ディズニーやピクサーだけじゃない！春休みにぴったり＜ディズニープラス＞おすすめコメディ・アクションアニメーション3選！",
            "img_url": "https://www.banger.jp/wp-content/uploads/2022/03/iceage-300x142.jpg",
            "created_at": "2022-03-29T07:00:38"
        },
        {
            "id": 76,
            "title": "ウィル・スミスがクリス・ロックに強烈ビンタ!! 二人は共演者であり長年の友人同士!? アカデミー賞授賞式から一夜明けてスミスが謝罪文を公開",
            "img_url": "https://www.banger.jp/wp-content/uploads/2022/03/shutterstock_347498957-300x200.jpg",
            "created_at": "2022-03-29T08:02:00"
        },
        {
            "id": 78,
            "title": "ディズニープラスが2022年4月の最新コンテンツ発表！国内アニメの見放題独占配信や日米韓ドラマ新作など盛りだくさん！",
            "img_url": "https://www.banger.jp/wp-content/uploads/2022/03/disneyplus-300x133.jpg",
            "created_at": "2022-03-25T03:56:22"
        },
        {
            "id": 80,
            "title": "Amazonプライム・ビデオ、2022年4月の新着コンテンツを発表！ 「ワイスピ」シリーズ最新作や人気マンガの待望のアニメ化「SPY×FAMILY」、劇場版『名探偵コナン』23作品一挙配信など見どころ満載!!",
            "img_url": "https://www.banger.jp/wp-content/uploads/2022/03/Amazon-Prime-Video-300x138.jpg",
            "created_at": "2022-03-28T07:48:02"
        },
        {
            "id": 88,
            "title": "第94回アカデミー賞ノミネート作品がYouTubeで観られる!? 映画館・配信サービスで視聴可能な作品を一挙ご紹介！",
            "img_url": "https://www.banger.jp/wp-content/uploads/2022/03/academy-1-300x144.jpg",
            "created_at": "2022-03-25T22:00:11"
        },
        {
            "id": 90,
            "title": "激レア！「バットマンとジョーカーの未公開シーン」解禁!! 大ヒット公開中の映画『THE BATMAN−ザ・バットマン−』",
            "img_url": "https://www.banger.jp/wp-content/uploads/2022/03/sc-300x125.jpg",
            "created_at": "2022-03-25T05:13:40"
        },
        {
            "id": 92,
            "title": "この春に、大スクリーンで“独特の世界観”を味わいたい映画5選！女王蜂・アヴちゃん×森山未來がW主演『犬王』公開記念！",
            "img_url": "https://www.banger.jp/wp-content/uploads/2022/03/8868dd0db74c5313e4767031f9bd08c8-300x125.jpg",
            "created_at": "2022-03-24T08:55:46"
        }
    ]

