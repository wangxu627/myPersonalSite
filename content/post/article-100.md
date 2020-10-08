
---
title: Angular项目集成eslint
date: 2020-01-06 06:35:37.919682
Description: ""
Tags: []
Categories: []
DisableComments: false
---
1.安装插件

    
    
    $ npm i -D eslint @typescript-eslint/{eslint-plugin,parser,eslint-plugin-tslint}

2.

    
    
    $ npx tslint-to-eslint-config

3.新建.eslintrc.js文件

    
    
    module.exports = {  
      "env": {  
          "browser": true,  
          "node": true  
      },  
      "extends": [],  
       "rules": {  
        'no-var': "error",  
        '@typescript-eslint/consistent-type-definitions': [  
            "error",  
            "interface"  
        ],  
        "padding-line-between-statements": [  
          "error",  
          { "blankLine": "always", "prev": "*", "next": "return" },  
          { "blankLine": "always", "prev": "function", "next": "function"}  
        ],  
        "lines-between-class-members": ["error", "always"]  
      },  
      "globals": {},  
      "parser": "@typescript-eslint/parser",  
      "parserOptions": {  
          "project": "tsconfig.json",  
          "sourceType": "module"  
      },  
      "plugins": [  
          "@typescript-eslint",  
          "@typescript-eslint/tslint"  
      ],  
      "settings": {}  
    };

4.执行

    
    
    ./node_modules/.bin/eslint "src/**/*.ts"

  

  

  


