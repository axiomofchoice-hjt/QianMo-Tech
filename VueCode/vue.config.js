const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
  devServer: {
    port: 8999, // 端口号的配置
    open: true // 自动打开浏览器
  },
  configureWebpack: {
    plugins: [
      new CopyWebpackPlugin([
          { from: 'node_modules/@liveqing/liveplayer/dist/component/crossdomain.xml'},
          { from: 'node_modules/@liveqing/liveplayer/dist/component/liveplayer-lib.min.js', to: 'js/'},
          { from: 'node_modules/@liveqing/liveplayer/dist/component/liveplayer.swf'}
      ])
    ]
  }
}
