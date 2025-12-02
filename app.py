import streamlit as st
import streamlit.components.v1 as components

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Audit Focus Mode",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. THEME: DIGITAL LEDGER (SPOTLIGHT EFFECT) ---
def inject_focus_theme():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;800&display=swap');

            :root {
                --bg-color: #0f172a;       /* Navy Blue đậm */
                --grid-color: #1e293b;     /* Slate 800 */
                --spotlight-color: rgba(56, 189, 248, 0.1); /* Light Blue Glow nhẹ */
            }

            .stApp {
                background-color: var(--bg-color);
                font-family: 'Manrope', sans-serif;
            }

            /* NỀN LƯỚI */
            .audit-grid-bg {
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background-image: 
                    linear-gradient(to right, var(--grid-color) 1px, transparent 1px),
                    linear-gradient(to bottom, var(--grid-color) 1px, transparent 1px);
                background-size: 40px 40px;
                z-index: 0; pointer-events: none;
            }

            /* SPOTLIGHT THEO CHUỘT */
            .spotlight-layer {
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: radial-gradient(
                    600px circle at var(--mouse-x, 50%) var(--mouse-y, 50%), 
                    var(--spotlight-color), transparent 40%
                );
                z-index: 1; pointer-events: none;
            }

            /* ẨN UI THỪA */
            #MainMenu, footer, header {visibility: hidden;}
            .block-container { padding-top: 5vh; max-width: 100%; position: relative; z-index: 10; }

            /* TYPOGRAPHY */
            .title-container { text-align: center; margin-bottom: 20px; }
            .main-title {
                font-size: 2.5rem; font-weight: 800; color: #f8fafc;
                letter-spacing: -1px; text-shadow: 0 4px 20px rgba(0,0,0,0.5);
            }
            .sub-title {
                color: #94a3b8; font-size: 1rem; letter-spacing: 2px;
                text-transform: uppercase; margin-top: 5px;
            }
            .status-pill {
                display: inline-flex; align-items: center; gap: 8px;
                background: rgba(15, 23, 42, 0.8); border: 1px solid #334155;
                padding: 8px 16px; border-radius: 99px; color: #38bdf8;
                font-size: 0.8rem; margin-top: 20px; backdrop-filter: blur(4px);
            }
            .pulse-dot {
                width: 8px; height: 8px; background-color: #38bdf8;
                border-radius: 50%; box-shadow: 0 0 10px #38bdf8;
                animation: pulse 2s infinite;
            }
            @keyframes pulse {
                0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; }
            }
        </style>

        <div class="audit-grid-bg"></div>
        <div class="spotlight-layer" id="spotlight"></div>

        <script>
            const spotlight = document.getElementById('spotlight');
            document.addEventListener('mousemove', (e) => {
                spotlight.style.setProperty('--mouse-x', e.clientX + 'px');
                spotlight.style.setProperty('--mouse-y', e.clientY + 'px');
            });
        </script>
    """, unsafe_allow_html=True)

# --- 3. HEYGEN COMPONENT (FIXED VISIBILITY) ---
def get_heygen_html_snippet():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>HeyGen AI</title>
      <style>
        body, html { margin: 0; padding: 0; background: transparent !important; overflow: hidden; height: 100%; width: 100%; }
        body { display: flex; justify-content: center; align-items: center; }
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
              
              /* TRẠNG THÁI THU GỌN */
              width: 160px; height: 160px;
              border-radius: 50%;
              overflow: hidden; 
              
              background-image: url('https://files2.heygen.ai/avatar/v3/74447a27859a456c955e01f21ef18216_45620/preview_talk_1.webp');
              background-size: cover;
              background-position: center 20%;
              
              border: 2px solid rgba(56, 189, 248, 0.5);
              box-shadow: 0 0 30px rgba(56, 189, 248, 0.2);
              
              transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
              opacity: 0; visibility: hidden;
              cursor: pointer;
          }

          #heygen-streaming-embed:hover {
              transform: translate(-50%, -50%) scale(1.08);
              box-shadow: 0 0 50px rgba(56, 189, 248, 0.4);
              border-color: #38bdf8;
          }

          /* --- SỬA LỖI MỜ Ở ĐÂY --- */
          #heygen-streaming-embed.expand {
              width: 100% !important; 
              height: 100% !important;
              max-width: 100% !important;
              
              border-radius: 8px; /* Bo góc nhẹ cho đẹp */
              border: 1px solid rgba(56, 189, 248, 0.3);
              
              /* FIX: Bỏ background màu và bỏ backdrop-filter */
              background: transparent !important;
              backdrop-filter: none !important;
              
              top: 0; left: 0;
              transform: none;
              box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
          }

          #heygen-streaming-container iframe { width: 100%; height: 100%; border: 0; position: absolute; top:0; left:0; }
          #heygen-streaming-embed.show { opacity: 1; visibility: visible; }
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
    inject_focus_theme()

    st.markdown("""
        <div class="title-container">
            <div class="sub-title">Audit Intelligence V3.1</div>
            <div class="main-title">VIRTUAL AUDIT ASSISTANT</div>
            <div class="status-pill">
                <div class="pulse-dot"></div>
                System Active & Ready to Analyze
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        components.html(get_heygen_html_snippet(), height=600, scrolling=False)

if __name__ == "__main__":
    main()