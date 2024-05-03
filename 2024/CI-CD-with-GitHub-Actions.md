# CI/CD with GitHub Actions

GitHub Actions is a CI/CD tool provided by GitHub. It is free for public repositories and has a free tier for private repositories as well. It is a very powerful tool and can be used to automate the workflow of your project. It can be used to build, test, and deploy your project. It can also be used to automate the release process of your project.

An example code,

```yml
name: hello-world
on: push
jobs: 
  hello-world-job:
    runs-on: ubuntu-latest
    steps: 
      - name: Check out repository code
        uses: actions/checkout@v3
      - run: echo "$(cat hello_world.txt)"
```

And an another one with a bit npm,

```yml
name: build-test-deploy
on: push
jobs: 
  build:
    runs-on: ubuntu-latest
    steps: 
      - name: checkout repo
        uses: actions/checkout@v3
      - name: use node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18.x'
      - run: npm install
      - run: npm run build 

  test: 
    needs: build
    runs-on: ubuntu-latest
    steps: 
      - name: checkout repo
        uses: actions/checkout@v3
      - name: use node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18.x'
      - run: npm install
      - run: npm test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    environment: 
      name: production
      url: ${{ steps.deployment.outputs.page_url }}
    permissions: 
      contents: write
      pages: write
      id-token: write
    steps:
      - name: checkout repo
        uses: actions/checkout@v3
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
      - name: use node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18.x'
      - name: configure github pages
        uses: actions/configure-pages@v3
        with:
          static_site_generator: next
      - run: npm install
      - run: npm run build 
      - name: upload artifacts
        uses: actions/upload-pages-artifact@v1
        with: 
          path: "./out"
      - name: deploy
        id: deployment
        uses: actions/deploy-pages@v1
```

This is a simple example of a GitHub Actions workflow that builds, tests, and deploys a project. The workflow is triggered on a push event. The workflow consists of three jobs: build, test, and deploy. The build job checks out the repository code, installs the dependencies, and builds the project. The test job checks out the repository code, installs the dependencies, and runs the tests. The deploy job checks out the repository code, installs the dependencies, builds the project, uploads the artifacts, and deploys the project to GitHub Pages.

Read more here,

- [Essentials of automated application deployment with GitHub Actions and GitHub Pages](https://resources.github.com/learn/pathways/automation/essentials/automated-application-deployment-with-github-actions-and-pages/)
