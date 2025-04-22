import { defineConfig, loadEnv } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";

export default ({ mode }) => {
  const env = loadEnv(mode, process.cwd());

  return defineConfig({
    plugins: [vue()],
    server: {
      proxy: {
        "/socket": {
          target: env.VITE_SOCKET_URL, // Use loaded env variable here
          changeOrigin: true,
          ws: true,
          rewrite: (path) => path.replace(/^\/socket/, ""),
        },
      },
    },
  });
};
