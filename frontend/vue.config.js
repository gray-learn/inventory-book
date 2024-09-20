const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  // Add the following configuration
  devServer: {
    proxy: {
      '/api': {
        //  use 127.0.0.1 instead of localhost on Windows
        target: 'http://127.0.0.1:8000',  // Django server
        secure: false,
        changeOrigin: true,
        pathRewrite: { '^/api': '' },  // Strips '/api' prefix if needed
      },

    },
  },
})
