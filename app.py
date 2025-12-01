import streamlit as st
import streamlit.components.v1 as components

# --- 1. SETUP PAGE CONFIG ---
st.set_page_config(
    page_title="HeyGen AI Assistant",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. ADVANCED CSS (THE "BEAUTY" LAYER) ---
def inject_immersive_css():
    st.markdown("""
        <style>
            /* IMPORT FONT */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

            /* RESET & BACKGROUND */
            .stApp {
                /* Tạo nền Gradient có chiều sâu thay vì đen kịt */
                background: radial-gradient(circle at 50% 10%, #1e202e 0%, #000000 100%);
                font-family: 'Inter', sans-serif;
            }

            /* ẨN CÁC THÀNH PHẦN THỪA CỦA STREAMLIT */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {
                padding-top: 3rem;
                padding-bottom: 0rem;
                max-width: 100%;
            }

            /* TIÊU ĐỀ CINEMATIC */
            .hero-title {
                text-align: center;
                font-size: 3rem;
                font-weight: 600;
                background: linear-gradient(90deg, #A1C4FD 0%, #C2E9FB 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0.5rem;
                letter-spacing: -1px;
                text-shadow: 0px 4px 12px rgba(0,0,0,0.5);
            }

            /* GLASSMORPHISM CARD (HIỆU ỨNG KÍNH) */
            .glass-card {
                background: rgba(255, 255, 255, 0.05); /* Trong suốt 5% */
                backdrop-filter: blur(12px);             /* Làm mờ hậu cảnh */
                -webkit-backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 20px 40px;
                text-align: center;
                max-width: 700px;
                margin: 0 auto 40px auto; /* Canh giữa */
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
                color: #E0E0E0;
            }

            .glass-card p {
                font-size: 1.1rem;
                margin: 0;
                line-height: 1.6;
            }

            .glass-card .highlight {
                color: #64B5F6;
                font-weight: 600;
            }

            .status-indicator {
                font-size: 0.85rem;
                color: #888;
                margin-top: 10px;
                display: block;
            }

            /* TỐI ƯU KHUNG IFRAME */
            iframe {
                border: none !important;
            }
        </style>
    """, unsafe_allow_html=True)

# --- 3. HEYGEN COMPONENT (OPTIMIZED VISUALS) ---
def get_heygen_html_snippet():
    # Chúng ta chỉnh sửa CSS bên trong HTML này để nút tròn đẹp hơn
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>HeyGen AI</title>
      <style>
        body, html { margin: 0; padding: 0; background-color: transparent; overflow: hidden; font-family: 'Inter', sans-serif; }
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
              position: absolute;
              left: 50%;
              bottom: 40px; /* Đẩy lên cao hơn một chút */
              transform: translateX(-50%);
              
              /* KÍCH THƯỚC BAN ĐẦU LỚN HƠN ĐỂ GÂY ẤN TƯỢNG */
              width: 180px;
              height: 180px;
              border-radius: 50%;
              
              /* VIỀN VÀ BÓNG PHÁT SÁNG (GLOW EFFECT) */
              border: 2px solid rgba(255, 255, 255, 0.3);
              box-shadow: 0 0 40px rgba(100, 181, 246, 0.3), inset 0 0 20px rgba(255,255,255,0.1);
              
              transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
              overflow: hidden;
              opacity: 0;
              visibility: hidden;
              
              background-image: url('https://files2.heygen.ai/avatar/v3/74447a27859a456c955e01f21ef18216_45620/preview_talk_1.webp');
              background-size: cover;
              background-position: center;
              cursor: pointer;
          }
          
          /* HIỆU ỨNG HOVER */
          #heygen-streaming-embed:hover {
              box-shadow: 0 0 60px rgba(100, 181, 246, 0.6);
              transform: translateX(-50%) scale(1.05);
          }

          #heygen-streaming-embed.show {
              opacity: 1;
              visibility: visible;
              animation: float 6s ease-in-out infinite; /* Avatar lơ lửng nhẹ */
          }

          #heygen-streaming-embed.expand {
              height: 550px; 
              width: 100%;
              max-width: 900px; /* Giới hạn chiều rộng để không bị vỡ hình */
              bottom: 20px;
              border: 1px solid rgba(255,255,255,0.1);
              border-radius: 20px;
              box-shadow: 0 20px 50px rgba(0,0,0,0.5);
              background-color: transparent;
              animation: none;
          }

          @keyframes float {
            0% { transform: translateX(-50%) translateY(0px); }
            50% { transform: translateX(-50%) translateY(-10px); }
            100% { transform: translateX(-50%) translateY(0px); }
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

# --- 4. MAIN APP LOGIC ---
def main():
    inject_immersive_css()

    # SECTION 1: HERO TITLE
    st.markdown('<div class="hero-title">Virtual AI Assistant</div>', unsafe_allow_html=True)

    # SECTION 2: GLASS CARD INSTRUCTION
    # Hướng dẫn được đặt trong khung kính mờ sang trọng
    st.markdown("""
        <div class="glass-card">
            <p>Chào mừng! Hãy nhấn vào <span class="highlight">Vòng tròn Avatar</span> bên dưới để bắt đầu cuộc trò chuyện.</p>
            <span class="status-indicator">● Ready to connect | Microphone access required</span>
        </div>
    """, unsafe_allow_html=True)

    # SECTION 3: THE AVATAR (CENTER STAGE)
    # Dùng 1 cột duy nhất, chiều cao full để tạo không gian
    # height=700 để đảm bảo khi avatar phóng to không bị thanh cuộn cắt
    components.html(get_heygen_html_snippet(), height=700, scrolling=False)

if __name__ == "__main__":
    main()