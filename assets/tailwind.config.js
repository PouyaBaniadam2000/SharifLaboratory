module.exports = {
    content: ["./public/**/*.{html,js}"],
    theme: {
      extend: {
        fontFamily: {
          'YekanBakh-Light': ['YekanBakh-Light'],
          'YekanBakh-Regular': ['YekanBakh-Regular'],
          'YekanBakh-SemiBold': ['YekanBakh-SemiBold'],
          'YekanBakh-Bold': ['YekanBakh-Bold'],
          'YekanBakh-ExtraBold': ['YekanBakh-ExtraBold'],
          'YekanBakh-ExtraBlack': ['YekanBakh-ExtraBlack'],
        },
      },
    },
    daisyui: {
      themes: ["light"],
      rtl: true,
    },
    plugins: [require("daisyui")],
  }