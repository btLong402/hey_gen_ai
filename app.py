import streamlit as st
import streamlit.components.v1 as components

# Cấu hình trang (Tùy chọn)
st.set_page_config(
    page_title="HeyGen AI Assistant",
    layout="wide"
)

# Giao diện chính của Streamlit
st.title("🤖 Ứng dụng Demo HeyGen AI")
st.write("Avatar AI sẽ xuất hiện trong khung bên dưới. Hãy đợi vài giây để kết nối.")
st.info("Lưu ý: Bạn cần cấp quyền truy cập Microphone khi trình duyệt yêu cầu để trò chuyện với Avatar.")

# --- ĐOẠN MÃ HEYGEN ---
# Tôi giữ nguyên đoạn HTML/JS bạn cung cấp, chỉ đưa vào biến string
heygen_html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>HeyGen AI Assistant</title>
</head>
<body>
  <script>
  !function(window){
      const host = "https://labs.heygen.com";
      const url = host + "/guest/streaming-embed?share=eyJxdWFsaXR5IjoiaGlnaCIsImF2YXRhck5hbWUiOiJNYXJpYW5uZV9DYXN1YWxMb29rX3B1Ymxp%0A%0AYyIsInByZXZpZXdJbWciOiJodHRwczovL2ZpbGVzMi5oZXlnZW4uYWkvYXZhdGFyL3YzLzA2ZmJj%0A%0ANTE5MDkyMzRkMDk5NmUwYTA1OTkxMTlhZDM0XzU1ODgwL3ByZXZpZXdfdGFyZ2V0LndlYnAiLCJu%0A%0AZWVkUmVtb3ZlQmFja2dyb3VuZCI6ZmFsc2UsImtub3dsZWRnZUJhc2VJZCI6IjYxZGViMDRmMzdm%0A%0AZjRmMmVhMTY0ZGM3MDcyYjcwNWIyIiwidXNlcm5hbWUiOiI5NWJmMjIyOTk4NWQ0MWVlYjAwNWY3%0A%0AZjUyNzVmZDZjZSJ9&inIFrame=1";

      const clientWidth = document.body.clientWidth;
      const wrapDiv = document.createElement("div");
      wrapDiv.id = "heygen-streaming-embed";

      const container = document.createElement("div");
      container.id = "heygen-streaming-container";

      const stylesheet = document.createElement("style");
      stylesheet.innerHTML = `
      #heygen-streaming-embed {
          z-index: 9999;
          position: fixed;
          left: 40px;
          bottom: 40px;
          width: 200px;
          height: 200px;
          border-radius: 50%;
          border: 2px solid #fff;
          box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.12);
          transition: all linear 0.1s;
          overflow: hidden;
          opacity: 0;
          visibility: hidden;
      }
      #heygen-streaming-embed.show {
          opacity: 1;
          visibility: visible;
      }
      #heygen-streaming-embed.expand {
          ${clientWidth < 540 
            ? "height: 266px; width: 96%; left: 50%; transform: translateX(-50%);" 
            : "height: 366px; width: calc(366px * 16 / 9);"}
          border: 0;
          border-radius: 8px;
      }
      #heygen-streaming-container {
          width: 100%;
          height: 100%;
      }
      #heygen-streaming-container iframe {
          width: 100%;
          height: 100%;
          border: 0;
      }
      `;

      const iframe = document.createElement("iframe");
      iframe.allowFullscreen = false;
      iframe.title = "Streaming Embed";
      iframe.role = "dialog";
      iframe.allow = "microphone";
      iframe.src = url;

      let visible = false;
      let initial = false;

      window.addEventListener("message", (e) => {
          if (e.origin === host && e.data && e.data.type === "streaming-embed") {
              if (e.data.action === "init") {
                  initial = true;
                  wrapDiv.classList.toggle("show", initial);
              } else if (e.data.action === "show") {
                  visible = true;
                  wrapDiv.classList.toggle("expand", visible);
              } else if (e.data.action === "hide") {
                  visible = false;
                  wrapDiv.classList.toggle("expand", visible);
              }
          }
      });

      container.appendChild(iframe);
      wrapDiv.appendChild(stylesheet);
      wrapDiv.appendChild(container);
      document.body.appendChild(wrapDiv);
  }(globalThis);
  </script>
</body>
</html>
"""

# Render HTML component
# height=600 là rất quan trọng để khi chatbox mở rộng không bị cắt
components.html(heygen_html_content, height=600, scrolling=False)

st.write("---")
st.caption("Bản quyền © HeyGen Streaming Avatar")