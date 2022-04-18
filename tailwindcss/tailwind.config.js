module.exports = {
  mode: "JIT",
  purge: ["../views/*.html"],
  content: [],
  theme: {
    extend: {
      fontFamily: {
        roboto: ["Roboto", "cursive"],
      },
      colors: {
        "theme": "#00acee",
        "blue1": "#1DA1F2",
        "blue2": "#2795D9",
        "blue": "#EFF9FF",
        "dark": "#657786",
        "input": "rgba(128, 128, 128, 0.486)",
        "light": "#AAB8C2",
        "lighter": "#E1E8ED",
        "lightest": "#F5F8FA",
      }
    },
  },
  plugins: [],
}
