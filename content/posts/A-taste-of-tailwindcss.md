+++
title = "A-taste-of-tailwindcss"
description = "Tailwindcss is a utility-first CSS framework. It is a low-level framework that provides you with all the building blocks you need to create a design system. It is a highly customizable framework that allows you to build designs without writing any CSS."
+++

# A taste of tailwindcss

Tailwindcss is a utility-first CSS framework. It is a low-level framework that provides you with all the building blocks you need to create a design system. It is a highly customizable framework that allows you to build designs without writing any CSS.

Enough right?

## CDN

You can use tailwindcss by including the CDN in your HTML file. You can include the following code in your HTML file to use tailwindcss.

```html
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
```

but what I did was to add,

```html
    <script src="https://cdn.tailwindcss.com"></script>
```

No big deal, just a script tag.

## NPM

### Tailwindcss CLI

> You can also use tailwindcss by installing it using npm. You can install tailwindcss using the following command.

But I just used npx and tailwindcss-cli to create a new project.

```bash
npx tailwindcss-cli build css/tailwind.css -o build/tailwind.css
```

And my css file actaually was,

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Vite

And I found an interesting way to use tailwindcss with vite. You can use the following command to install tailwindcss with vite.

```bash
 npm init -y
 ```

 And then comes dependencies,

 ```bash
 npm install -D tailwindcss postcss autoprefixer vite            
 ```

 Later on, you can create a tailwind.config.js file and add the following code to it.

 ```js
    module.exports = {
    purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {},
    },
    variants: {
        extend: {},
    },
    plugins: [],
    }
```

Or, this command should do the trick,

```bash
npx tailwindcss init -p
```

And my `package.json` file was,

```json
{
  "name": "tailwind",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "dev": "vite"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "devDependencies": {
    "autoprefixer": "^10.4.19",
    "postcss": "^8.4.38",
    "tailwindcss": "^3.4.3",
    "vite": "^5.2.12"
  }
}
```

Interesting right? Maybe afterwards,

```bash
npm run dev
```

> I was needed to run `npm install` to install the dependencies once more.

### Building css

For now, I changed my css file to,

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
    .btn {
        @apply mt-4 inline-block bg-indigo-500 px-5 py-4 shadow-lg rounded-lg uppercase tracking-wider text-white font-semibold text-sm sm:text-base hover:bg-indigo-600 transition duration-300 ease-in-out transform transition hover:-translate-y-1 hover:shadow-xl
    }
}
```

But I was needed to run the following command to build the css file.

```bash
npx tailwindcss-cli build css/tailwind.css -o build/tailwind.css
```

So tweaked my `package.json` file to include the following command.

```json
{
  "name": "tailwind",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "build": "vite build", 
    "build-css": "npx tailwindcss-cli build css/tailwind.css -o build/tailwind.css", 
    "dev": "vite"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "devDependencies": {
    "autoprefixer": "^10.4.19",
    "postcss": "^8.4.38",
    "tailwindcss": "^3.4.3",
    "vite": "^5.2.12"
  }
}
```

