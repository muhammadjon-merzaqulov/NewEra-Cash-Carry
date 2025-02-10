<h1>NewEra-Cash-Carry</h1>

<p>Bu loyiha do'konni boshqarish tizimi uchun yaratilgan Python dasturidir. Ushbu tizimda foydalanuvchilar turli rollarga ega: mijoz, admin va superadmin. Har bir rol o'ziga xos funktsiyalar va imkoniyatlarga ega bo'lib, tizim orqali foydalanuvchilar ma'lumotlarini boshqarish mumkin.</p>

<h2>Asosiy imkoniyatlar</h2>
<ul>
    <li><strong>Mijozlar</strong> tizimga kirib, o'z profilingizni ko'rish va yangilash imkoniyatiga ega bo'lishadi.</li>
    <li><strong>Admin</strong> foydalanuvchilarga boshqaruv ruxsatlarini beradi, mahsulotlarni va buyurtmalarni boshqaradi.</li>
    <li><strong>Superadmin</strong> yuqori darajadagi boshqaruv ruxsatlariga ega bo'lib, tizimning barcha funksiyalarini boshqaradi.</li>
</ul>

<h2>Ma'lumotlar bazasini tayyorlash</h2>
<p>Dasturda ma'lumotlarni saqlash uchun SQLite ma'lumotlar bazasidan foydalaniladi. Dastur ishga tushirilganda, <code>store.db</code> nomli ma'lumotlar bazasi yaratiladi va foydalanuvchi ma'lumotlari saqlanadi.</p>

<h2>Virtual Muhit</h2>
<p>Agar siz virtual muhitdan foydalanishni xohlasangiz, quyidagicha virtual muhit yaratib, faollashtiring:</p>

<h3>Virtual muhit yaratish:</h3>
<pre><code>python -m venv venv</code></pre>

<h3>Virtual muhitni faollashtirish:</h3>
<ul>
    <li><strong>Mac/Linux:</strong> <code>source venv/bin/activate</code></li>
    <li><strong>Windows:</strong> <code>.\venv\Scripts\activate</code></li>
</ul>

<h2>Foydalanish</h2>

<h3>Dasturga kirish:</h3>
<p>Dastur ishga tushirilganda foydalanuvchi loginini kiritadi. Agar foydalanuvchi tizimda mavjud bo'lsa, parolni kiritish talab qilinadi. Agar foydalanuvchi yangi bo'lsa, tizim yangi foydalanuvchi yaratish uchun imkoniyat beradi.</p>

<h3>Foydalanuvchining roli:</h3>
<p>Tizim foydalanuvchining rolini aniqlaydi: mijoz, admin yoki superadmin. Tegishli rolga qarab, foydalanuvchiga mos menyu ko'rsatiladi.</p>

<ul>
    <li><strong>Mijozlar</strong> o'z profilingizni ko'rish va yangilash imkoniyatiga ega.</li>
    <li><strong>Adminlar</strong> foydalanuvchilarni boshqarish va mahsulotlar bilan ishlash imkoniyatiga ega.</li>
    <li><strong>Superadminlar</strong> tizimning barcha funksiyalarini boshqaradi va yuqori darajadagi ruxsatlarni belgilaydi.</li>
</ul>

<h2>Tizimda ishlash</h2>
<p>Tizimda ro'yxatdan o'tgan foydalanuvchilarning ma'lumotlari <code>store.db</code> SQLite ma'lumotlar bazasida saqlanadi.</p>

<h2>Mualliflar</h2>
<ul>
    <li><a href="https://github.com/muhammadjon-merzaqulov">Muhammadjon Merzaqulov</a></li>
</ul>

<h2>Litsenziya</h2>
<p>Bu loyiha <strong>MIT Litsenziyasi</strong> asosida litsenziyalangan.</p>
