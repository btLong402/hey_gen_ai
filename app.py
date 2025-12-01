import streamlit as st
import streamlit.components.v1 as components

# --- 1. SETUP PAGE ---
st.set_page_config(
    page_title="HeyGen AI Futuristic",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. FUTURISTIC UI & MOUSE EFFECT ---
def inject_sci_fi_css():
    st.markdown("""
        <style>
            /* IMPORT FONT */
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400&display=swap');

            /* --- BACKGROUND: CYBER GRID --- */
            .stApp {
                background-color: #050505;
                background-image: 
                    linear-gradient(rgba(30, 30, 30, 0.3) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(30, 30, 30, 0.3) 1px, transparent 1px);
                background-size: 40px 40px; /* Kích thước ô lưới */
                background-position: center top;
            }

            /* --- MOUSE GLOW FOLLOWER (Hiệu ứng con trỏ) --- */
            /* Ta tạo một div ảo di chuyển theo chuột */
            #glow-cursor {
                position: fixed;
                width: 300px;
                height: 300px;
                background: radial-gradient(circle, rgba(0, 255, 255, 0.15) 0%, rgba(0, 0, 0, 0) 70%);
                border-radius: 50%;
                pointer-events: none; /* Không chặn click chuột */
                transform: translate(-50%, -50%);
                z-index: 0;
                mix-blend-mode: screen;
                transition: transform 0.1s ease-out; /* Mượt mà */
            }

            /* ẨN UI THỪA */
            #MainMenu, footer, header {visibility: hidden;}
            
            /* TỐI ƯU LAYOUT */
            .block-container {
                padding-top: 2rem;
                padding-bottom: 0rem;
                max-width: 100%;
            }

            /* TYPOGRAPHY */
            .sci-fi-title {
                font-family: 'Orbitron', sans-serif; /* Font kiểu điện tử */
                text-align: center;
                font-size: 2.5rem;
                font-weight: 700;
                color: #fff;
                text-transform: uppercase;
                letter-spacing: 4px;
                margin-bottom: 0px;
                text-shadow: 0 0 10px rgba(0, 255, 255, 0.7);
            }

            .sci-fi-subtitle {
                font-family: 'Inter', sans-serif;
                text-align: center;
                color: #aaa;
                font-size: 0.9rem;
                margin-bottom: 20px;
            }

            /* GLASS CARD COMPACT */
            .glass-panel {
                background: rgba(10, 20, 30, 0.6);
                border: 1px solid rgba(0, 255, 255, 0.2);
                border-radius: 12px;
                padding: 10px 30px;
                display: inline-block;
                backdrop-filter: blur(5px);
                box-shadow: 0 0 15px rgba(0, 255, 255, 0.1);
            }

        </style>
        
        <div id="glow-cursor"></div>
        <script>
            const cursor = document.getElementById('glow-cursor');
            document.addEventListener('mousemove', (e) => {
                cursor.style.left = e.clientX + 'px';
                cursor.style.top = e.clientY + 'px';
            });
        </script>
    """, unsafe_allow_html=True)

# --- 3. HEYGEN COMPONENT (RESIZED & CENTERED) ---
def get_heygen_html_snippet():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>HeyGen AI</title>
      <style>
        body, html { margin: 0; padding: 0; background: transparent; overflow: hidden; height: 100%; display: flex; justify-content: center; align-items: center; }
      </style>
    </head>
    <body>
      <script>
      !function(window){
          const host = "https://labs.heygen.com";
          const url=host+"/guest/streaming-embed?share=eyJxdWFsaXR5IjoiaGlnaCIsImF2YXRhck5hbWUiOiJKdW5lX0hSX3B1YmxpYyIsInByZXZpZXdJ%0D%0AbWciOiJodHRwczovL2ZpbGVzMi5oZXlnZW4uYWkvYXZhdGFyL3YzLzc0NDQ3YTI3ODU5YTQ1NmM5%0D%0ANTVlMDFmMjFlZjE4MjE2XzQ1NjIwL3ByZXZpZXdfdGFsa18xLndlYnAiLCJuZWVkUmVtb3ZlQmFj%0D%0Aa2dyb3VuZCI6ZmFsc2UsImtub3dsZWRnZUJhc2VJZCI6IjYxZGViMDRmMzdmZjRmMmVhMTY0ZGM3%0D%0AMDcyYjcwNWIyIiwidXNlcm5hbWUiOiI5NWJmMjIyOTk4NWQ0MWVlYjAwNWY3ZjUyNzVmZDZjZSJ9&inIFrame=1";

          const wrapDiv = document.createElement("div");
          wrapDiv.id = "heygen-streaming-embed";
          const container = document.createElement("div");
          container.id = "heygen-streaming-container";

          const stylesheet = document.createElement("style");
          stylesheet.innerHTML = `
          #heygen-streaming-embed {
              z-index: 9999;
              position: absolute;
              top: 50%; left: 50%;
              transform: translate(-50%, -50%);
              
              /* KÍCH THƯỚC NÚT TRÒN BAN ĐẦU */
              width: 140px; height: 140px;
              border-radius: 50%;
              border: 2px solid rgba(0, 255, 255, 0.5); /* Viền màu Cyan */
              box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
              
              transition: all 0.4s ease-in-out;
              opacity: 0; visibility: hidden;
              background-image: url('https://files2.heygen.ai/avatar/v3/74447a27859a456c955e01f21ef18216_45620/preview_talk_1.webp');
              background-size: cover; background-position: center;
              cursor: pointer;
          }
          
          /* Hiệu ứng Pulse khi chờ đợi */
          @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(0, 255, 255, 0.4); }
            70% { box-shadow: 0 0 0 20px rgba(0, 255, 255, 0); }
            100% { box-shadow: 0 0 0 0 rgba(0, 255, 255, 0); }
          }
          #heygen-streaming-embed.show {
              opacity: 1; visibility: visible;
              animation: pulse 2s infinite;
          }

          /* KHI MỞ RỘNG - GIỚI HẠN KÍCH THƯỚC ĐỂ VỪA KHUNG */
          #heygen-streaming-embed.expand {
              width: 100%; 
              height: 100%;
              max-width: 800px; /* Giới hạn chiều rộng ngang */
              border-radius: 10px;
              border: 1px solid rgba(0, 255, 255, 0.2);
              box-shadow: 0 0 40px rgba(0, 0, 0, 0.6);
              animation: none;
              background: #000;
          }

          #heygen-streaming-container iframe { width: 100%; height: 100%; border: 0; }
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

# --- 4. MAIN APP ---
def main():
    inject_sci_fi_css()

    # Header Section
    st.markdown('<div class="sci-fi-title">AI CORE INTERFACE</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center;">
            <div class="glass-panel">
                <span style="color: #0ff;">SYSTEM READY</span> &nbsp;|&nbsp; CLICK AVATAR TO INITIALIZE
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Avatar Section - ĐIỀU CHỈNH QUAN TRỌNG
    # Giảm height xuống 520px để vừa vặn màn hình mà không cần cuộn
    col1, col2, col3 = st.columns([1, 10, 1])
    
    with col2:
        components.html(get_heygen_html_snippet(), height=520, scrolling=False)

if __name__ == "__main__":
    main()