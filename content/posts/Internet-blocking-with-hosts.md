+++
title = "Internet-blocking-with-hosts"
description = "এই ফাইল মূলত কোনো একটা address (URL) কে অন্য কোনো address এ redirect করতে ব্যবহৃত হয়। এর সবচেয়ে বাস্তবিক প্রয়োগ হচ্ছে adblocking এর ক্ষেত্রে। যেসব website আমরা block করতে চাই, সেসব website কে আমরা 0.0.0.0 (localhost) এ forward করি, এই ফরম্যাটে,"
+++

# Internet blocking with hosts

## Hostfile

এই ফাইল মূলত কোনো একটা address (URL) কে অন্য কোনো address এ redirect করতে ব্যবহৃত হয়। এর সবচেয়ে বাস্তবিক প্রয়োগ হচ্ছে adblocking এর ক্ষেত্রে। যেসব website আমরা block করতে চাই, সেসব website কে আমরা 0.0.0.0 (localhost) এ forward করি, এই ফরম্যাটে,

```bash
127.0.0.1       localhost
0.0.0.0         যাকে_ব্লক_করতে_চাই.com
```

> এভাবে একটা একটা করে সাইট ব্লক করা যায়। যদি আপনি চান একটি নির্দিষ্ট সাইট ছাড়া বাকি সব ব্লক হবে তাহলে firewall rule set করতে হবে। তবে hostfile, firewall থেকে বেশী সহজ ও নিরাপদ।

আরো বিস্তারিত জানতে এই link টি দেখতে পারেন,

- <https://man.archlinux.org/man/hosts.5>

### Linux

লিনাক্স ফাইলসিস্টেমে host file এর location,

```bash
/etc/hosts
```

### Windows

উইন্ডোজ ফাইলসিস্টেমে host file এর location,

```bash
C:\Windows\System32\drivers\etc\hosts
```

> পাশাপাশি আমি একটা batch script লিখেছি, এটাও দেখতে পারেন, সাধারণত এটা লেখা হয়েছে একটা কনটেস্ট কে সামনে রেখে (toph.co ভিন্ন বাকি অনেক সাইট, যেমন vscode extension, ব্লক করবে যা contest এর জন্য সীমাবদ্ধ)। এর দ্বিতীয় option দ্বারা hostfile পূর্বাবস্থায় নিয়ে যাওয়া যাবে।
>
> - <https://gist.github.com/SharafatKarim/f50f6ca40d2411689573152798198c74>

## যদি host file এ delete করি?

তাহলে internet simply unblock হয়ে যাবে, as simple as that!

## একটা বাস্তব প্রয়োগ?

এই GitHub repository টি দেখতে পারেন, এখানে বিজ্ঞাপন ও অপ্রাসঙ্গিক website গুলো ব্লক করার জন্য একটা বড়সড় collection আছে।

- <https://github.com/StevenBlack/hosts>

এখানকার `hosts` নামের ফাইলটি কপি করে যদি আপনার OS অনুযায়ী সেট করেন, auto সব ad block হবে। ব্রাউজারে কোনো আলাদা extension লাগবে না। এমনিতেও বর্তমানে chrome browser, ublock origin সমর্থন করবে না (manifest v3 fact)।

