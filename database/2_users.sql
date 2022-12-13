INSERT INTO users
    (e_mail,password,created_at,updated_at)
VALUES
    ("test@test.com", "pbkdf2:sha256:150000$U75TOl4m$1ceb173704ad5d811db35a7e3b661ef23594758ce747f4f0ca9f664604c404d8", "2020-07-21 20:00:00", "2020-07-21 20:00:00");
-- パスワードはpassword

INSERT INTO users
    (e_mail,password,created_at,updated_at)
VALUES
    ("test2@test.com", "pbkdf2:sha256:150000$cSs8pQro$ab98c662a85d7781d0568e3ca70442db81416f7c1719dea1388afbec2c4c1d67", "2020-07-22 22:00:00", "2020-07-22 22:00:00");
-- パスワードはpassword2

-- 生成方法
-- $ python
-- >>> from werkzeug.security import generate_password_hash
-- >>> generate_password_hash('password')
-- 'pbkdf2:sha256:150000$U75TOl4m$1ceb173704ad5d811db35a7e3b661ef23594758ce747f4f0ca9f664604c404d8'
-- >>> generate_password_hash('password2')
-- 'pbkdf2:sha256:150000$cSs8pQro$ab98c662a85d7781d0568e3ca70442db81416f7c1719dea1388afbec2c4c1d67'