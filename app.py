import streamlit as st
import streamlit.components.v1 as components

# --- 1. CONFIGURATION & SETUP ---
st.set_page_config(
    page_title="HeyGen AI Assistant",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed" # Ẩn sidebar để màn hình rộng hơn
)

# --- 2. CSS OPTIMIZATION (HACKING THE UI) ---
# Loại bỏ header, footer, padding thừa để giao diện giống một Web App thực thụ
def inject_custom_css():
    st.markdown("""
        <style>
            /* Ẩn Main Menu (Hamburger) và Footer */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Tối ưu khoảng cách lề (Padding) */
            .block-container {
                padding-top: 2rem;
                padding-bottom: 0rem;
                padding-left: 2rem;
                padding-right: 2rem;
            }
            
            /* Tạo hiệu ứng Card cho phần hướng dẫn */
            .info-card {
                background-color: #f0f2f6;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                margin-bottom: 20px;
                text-align: center;
            }
            
            /* Tùy chỉnh tiêu đề */
            h1 {
                color: #2E4053;
                font-family: 'Helvetica Neue', sans-serif;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

# --- 3. COMPONENT LOGIC ---
def get_heygen_html_snippet():
    """
    Trả về chuỗi HTML/JS của HeyGen. 
    Đã tối ưu hóa CSS nội bộ để Avatar hiển thị đẹp hơn trong iframe.
    """
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>HeyGen AI</title>
      <style>
        /* Đảm bảo nền trong suốt để hòa trộn với Streamlit */
        body, html { margin: 0; padding: 0; background-color: transparent; overflow: hidden; }
      </style>
    </head>
    <body>
      <script>
      !function(window){
          const host = "https://labs.heygen.com";
          const url=host+"/guest/streaming-embed?share=eyJxdWFsaXR5IjoiaGlnaCIsImF2YXRhck5hbWUiOiJKdW5lX0hSX3B1YmxpYyIsInByZXZpZXdJ%0D%0AbWciOiJodHRwczovL2ZpbGVzMi5oZXlnZW4uYWkvYXZhdGFyL3YzLzc0NDQ3YTI3ODU5YTQ1NmM5%0D%0ANTVlMDFmMjFlZjE4MjE2XzQ1NjIwL3ByZXZpZXdfdGFsa18xLndlYnAiLCJuZWVkUmVtb3ZlQmFj%0D%0Aa2dyb3VuZCI6ZmFsc2UsImtub3dsZWRnZUJhc2VJZCI6IjYxZGViMDRmMzdmZjRmMmVhMTY0ZGM3%0D%0AMDcyYjcwNWIyIiwidXNlcm5hbWUiOiI5NWJmMjIyOTk4NWQ0MWVlYjAwNWY3ZjUyNzVmZDZjZSJ9&inIFrame=1";

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
              /* ĐIỀU CHỈNH VỊ TRÍ: Đưa ra giữa hoặc góc đẹp hơn */
              left: 50%;
              bottom: 20px;
              transform: translateX(-50%); /* Căn giữa theo chiều ngang */
              
              width: 200px;
              height: 200px;
              border-radius: 50%;
              border: 3px solid #ffffff;
              box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2);
              transition: all linear 0.1s;
              overflow: hidden;
              opacity: 0;
              visibility: hidden;
              background-image: url('https://files2.heygen.ai/avatar/v3/74447a27859a456c955e01f21ef18216_45620/preview_talk_1.webp'); /* Ảnh nền chờ */
              background-size: cover;
          }
          #heygen-streaming-embed.show {
              opacity: 1;
              visibility: visible;
          }
          #heygen-streaming-embed.expand {
              /* Khi mở rộng, chiếm phần lớn khung hình iframe */
              height: 500px; 
              width: 90%;
              left: 50%;
              bottom: 50px;
              transform: translateX(-50%);
              border: 0;
              border-radius: 12px;
              background-color: transparent;
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

# --- 4. MAIN APPLICATION ---
def main():
    inject_custom_css()
    
    # UI: Header Section
    st.markdown("<h1>🤖 Trợ lý Ảo AI HeyGen</h1>", unsafe_allow_html=True)
    
    # UI: Instruction Card
    st.markdown("""
        <div class="info-card">
            <p><strong>Hướng dẫn:</strong> Nhấn vào hình tròn bên dưới (sau khi tải xong) để bắt đầu trò chuyện.</p>
            <small style="color: #666;">⚠️ Vui lòng cấp quyền Microphone khi trình duyệt yêu cầu.</small>
        </div>
    """, unsafe_allow_html=True)

    # UI: Avatar Container
    # Chúng ta sử dụng 3 cột để căn giữa iframe chứa avatar
    col1, col2, col3 = st.columns([1, 6, 1])
    
    with col2:
        # Render Avatar
        # height=650 phải đủ lớn để chứa trạng thái "expand" của Avatar
        components.html(get_heygen_html_snippet(), height=650, scrolling=False)

if __name__ == "__main__":
    main()