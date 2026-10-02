const args = process.argv.slice(2);
const command = args[0];

if (command === "مرحبا") {
    console.log("مرحباً بك باستخدام JavaScript!");
} else if (command === "حساب") {
    const num1 = parseFloat(args[1]) || 0;
    const num2 = parseFloat(args[2]) || 0;
    console.log("الناتج:", num1 + num2);
} else {
    console.log("الرجاء إدخال أمر صحيح (مرحبا أو حساب).");
}
