# NewEra-Cash-Carry
<p>Bu loyiha do'konni boshqarish tizimi uchun Python dasturi. Tizimda foydalanuvchi login va parol yordamida tizimga kiradi. Tizimda uchta turdagi foydalanuvchi mavjud: mijoz, admin va superadmin.</p>

<h2>Tizimning asosiy imkoniyatlari</h2>
<ul>
    <li><strong>Mijozlar:</strong> Tizimga kirib, o'z profilingizni ko'rish va yangilash imkoniyatiga ega.</li>
    <li><strong>Admin:</strong> Foydalanuvchilarga boshqaruv ruxsatlarini beradi va do'konni boshqaradi.</li>
    <li><strong>Superadmin:</strong> Yuqori darajadagi boshqaruv ruxsatlariga ega va tizimning asosiy boshqaruvchisidir.</li>
</ul>

<h2>O‘rnatish</h2>
<p>Dasturga kerakli kutubxonalarni o'rnatish:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<p>SQLite ma'lumotlar bazasini yaratish (agar hali mavjud bo'lmasa):</p>
<p>store.db faylini yaratish va unga foydalanuvchi ma'lumotlarini saqlash uchun kerakli jadval va ma'lumotlarni joylashtirish.</p>

<h2>Foydalanish</h2>
<ol>
    <li>Dastur ishga tushganda foydalanuvchi loginini kiritadi.</li>
    <li>Agar foydalanuvchi tizimda mavjud bo'lsa, parolni kiritish talab qilinadi.</li>
    <li>Agar foydalanuvchi yangi bo'lsa, tizim yangi foydalanuvchi yaratish uchun imkoniyat beradi.</li>
    <li>Tizim foydalanuvchining rolini tekshiradi (mijoz, admin yoki superadmin) va mos ravishda tegishli menyu ko'rsatiladi.</li>
</ol>

<h2>Tizimda ishlash</h2>
<p>Tizimda ro'yxatdan o'tgan foydalanuvchilarning ma'lumotlari <code>store.db</code> SQLite ma'lumotlar bazasida saqlanadi.</p>

<h3>menu.py fayl</h3>
<ul>
    <li><strong>admin_menu:</strong> Admin foydalanuvchi uchun menyu.</li>
    <li><strong>customer_menu:</strong> Mijoz foydalanuvchi uchun menyu.</li>
    <li><strong>superadmin_menu:</strong> Superadmin foydalanuvchi uchun menyu.</li>
</ul>

<h3>query.py fayl</h3>
<ul>
    <li><strong>have_user(username):</strong> Foydalanuvchi tizimda mavjudligini tekshiradi.</li>
    <li><strong>get_role(username, password):</strong> Foydalanuvchining rolini aniqlaydi.</li>
    <li><strong>add_user(username, password):</strong> Yangi foydalanuvchi qo'shadi.</li>
</ul>

<h2>Mualliflar</h2>
    <ul>
        <li><a href="https://github.com/muhammadjon-merzaqulov">Muhammadjon Merzaqulov</a></li>
    </ul>

    <h2>Litsenziya</h2>
    <p>Bu loyiha <strong>MIT Litsenziyasi</strong> asosida litsenziyalangan.</p>
