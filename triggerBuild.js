#!/usr/bin/env node
"use strict";

const shell = require('shelljs'),
  path = require('path'),
  got = require('got');

const subprocess = require('child_process').exec;

console.log(`Fetching Git commit hash...`);

console.log(`blah`);
const gitCommitRet = subprocess('ls', function(error, stdout, stderr){
  cwd: path.join(__dirname, '..', 'postman_travis');
  console.log(stdout);
})

// const gitCommitRet = subprocess('ls', (error, stdout, stderr) => {
//   console.log("testtt")
//
//   console.log(`stdout: ${stdout}`);
//   console.log(`stderr: ${stderr}`);
// });

// const gitCommitRet = shell.exec('git rev-parse HEAD', {
//   console.log("blah");
//   cwd: path.join(__dirname, '..', 'postman_travis');
//
// });

if (0 !== gitCommitRet.code) {
  console.error('Error getting git commit hash');

  process.exit(-1);
}

const gitCommitHash = gitCommitRet.stdout.trim();

console.log(`Git commit: ${gitCommitHash}`);

console.log('Calling Travis...');


got.post(`https://api.travis-ci.org/repo/waigo%2Fwaigo.github.io/requests`, {
  headers: {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Travis-API-Version": "3",
    "Authorization": `token ${process.env.TRAVIS_API_TOKEN}`,
  },
  body: JSON.stringify({
    request: {
      message: `Trigger build at fayeezahmed/postman_travis commit: ${gitCommitHash}`,
      branch: 'source',
    },
  }),
})
.then(() => {
  console.log("Triggered build of fayeezahmed/postman_travis.git");
})
.catch((err) => {
  console.error(err);

  process.exit(-1);
});
