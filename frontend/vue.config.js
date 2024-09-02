const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
	devServer: {
		webSocketServer: false,// ws 사용 X
	},
});
module.exports = defineConfig({
  transpileDependencies: true,

  pluginOptions: {
    vuetify: {
			// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
		}
  }
})
