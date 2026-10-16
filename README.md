# SHADOW DEMON — Android starter project

واجهة Android أولية باللغة العربية بتصميم أسود/أحمر، تتضمن الرئيسية والمقاطع القصيرة ومكتبة الأنمي والمفضلة والإعدادات.

## البناء
- افتح المجلد في Android Studio حديث.
- اسمح له بمزامنة Gradle وتنزيل Android SDK Platform 35 عند الطلب.
- من قائمة Build اختر Build APK(s).
- الملف الناتج عادةً: `app/build/outputs/apk/debug/app-debug.apk`

## ملاحظات
هذه نسخة واجهة أولية تعمل بمحتوى تجريبي، وليست خدمة بث أو تنزيل فيديو حقيقية. لا تتضمن مصادر محتوى أو تنزيلات غير مرخّصة. الأيقونة متوفرة في `app/src/main/res/drawable/shadow_demon_icon.png`.

## Build APK in GitHub Actions (if local Android Studio is unavailable)
1. Create a GitHub repository and upload the contents of this project.
2. Open the repository's **Actions** tab and run **Build Shadow Demon APK**.
3. When the workflow succeeds, open its run and download the `shadow-demon-debug-apk` artifact.
4. Extract the ZIP on the Android phone and tap `app-debug.apk` to install. Android may ask you to allow installs from that source.
