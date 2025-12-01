import streamlit as st
import streamlit.components.v1 as components

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Audit Intelligence Assistant",
    page_icon="xp",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CORPORATE CSS (THE "BIG 4" LOOK) ---
def inject_corporate_css():
    st.markdown("""
        <style>
            /* IMPORT PROFESSIONAL FONTS */
            @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&family=Playfair+Display:wght@700&display=swap');

            /* --- BACKGROUND: CLEAN & PROFESSIONAL --- */
            .stApp {
                background-color: #f4f6f9; /* Xám xanh nhạt rất dịu mắt */
                background-image: linear-gradient(135deg, #f4f6f9 0%, #eef2f3 100%);
                font-family: 'Lato', sans-serif;
                color: #2c3e50;
            }

            /* ẨN UI THỪA */
            #MainMenu, footer, header {visibility: hidden;}
            .block-container { padding-top: 3rem; padding-bottom: 0rem; max-width: 100%; }

            /* --- HEADER SECTION --- */
            .audit-header {
                text-align: center;
                margin-bottom: 30px;
                padding-bottom: 20px;
                border-bottom: 1px solid #d1d8e0;
            }

            .audit-title {
                font-family: 'Playfair Display', serif; /* Font có chân tạo uy quyền */
                font-size: 2.5rem;
                font-weight: 700;
                color: #0f2027; /* Deep Navy */
                margin: 0;
                letter-spacing: 0.5px;
            }

            .audit-subtitle {
                font-family: 'Lato', sans-serif;
                font-size: 0.95rem;
                color: #57606f;
                text-transform: uppercase;
                letter-spacing: 2px;
                margin-top: 5px;
            }

            /* --- PROFESSIONAL CARD --- */
            .corp-card {
                background: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.05); /* Bóng đổ rất nhẹ */
                border-left: 5px solid #205072; /* Đường viền xanh bên trái tạo điểm nhấn */
                padding: 20px 40px;
                max-width: 700px;
                margin: 0 auto 30px auto;
                text-align: center;
            }

            .corp-card p {
                margin: 0;
                font-size: 1rem;
                color: #333;
                line-height: 1.6;
            }
            
            .highlight-text {
                color: #205072;
                font-weight: 700;
            }

            /* --- STATUS BADGE --- */
            .status-badge {
                display: inline-block;
                margin-top: 10px;
                padding: 4px 12px;
                background-color: #e8f5e9;
                color: #2e7d32;
                border-radius: 100px;
                font-size: 0.75rem;
                font-weight: 600;
                border: 1px solid #c8e6c9;
            }

        </style>
    """, unsafe_allow_html=True)

# --- 3. HEYGEN COMPONENT (OFFICE STYLE) ---
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
              z-index: 2147483647;
              position: absolute;
              top: 50%; left: 50%;
              transform: translate(-50%, -50%);
              
              /* STYLE CHO TRẠNG THÁI THU GỌN: CHUYÊN NGHIỆP */
              width: 140px; height: 140px;
              border-radius: 50%;
              overflow: hidden; 
              
              /* Ảnh nền */
              background-image: url('https://files2.heygen.ai/avatar/v3/74447a27859a456c955e01f21ef18216_45620/preview_talk_1.webp');
              background-size: cover;
              background-position: center 20%;
              
              /* Viền kép tạo cảm giác trang trọng */
              border: 4px solid #fff;
              box-shadow: 0 8px 24px rgba(32, 80, 114, 0.25); /* Bóng màu xanh navy */
              
              transition: all 0.4s ease;
              opacity: 0; visibility: hidden;
              cursor: pointer;
          }

          /* Hiệu ứng Hover nhẹ nhàng, lịch sự */
          #heygen-streaming-embed:hover {
              transform: translate(-50%, -50%) scale(1.05);
              box-shadow: 0 12px 30px rgba(32, 80, 114, 0.35);
              border-color: #f1f2f6;
          }

          /* TRẠNG THÁI MỞ RỘNG (EXPAND) */
          #heygen-streaming-embed.expand {
              width: 100% !important; 
              height: 100% !important;
              max-width: 100% !important;
              max-height: 100% !important;
              
              border-radius: 0;
              border: none;
              box-shadow: none;
              background: transparent; 
              background-image: none;
              
              top: 0; left: 0;
              transform: none;
          }

          #heygen-streaming-container { width: 100%; height: 100%; }
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
    inject_corporate_css()

    # HEADER: Logo và Tên hệ thống
    st.markdown("""
        <div class="audit-header">
            <h1 class="audit-title">AUDIT INTELLIGENCE SUITE</h1>
            <div class="audit-subtitle">Financial Analysis &bullet; Risk Assurance &bullet; Compliance</div>
        </div>
    """, unsafe_allow_html=True)

    # INFO CARD: Hướng dẫn ngắn gọn
    st.markdown("""
        <div class="corp-card">
            <p>Chào bạn, tôi là <span class="highlight-text">Trợ lý Kiểm toán Ảo</span>.</p>
            <p style="font-size: 0.9rem; color: #666; margin-top: 5px;">
                Vui lòng nhấn vào hình đại diện bên dưới để bắt đầu phiên tư vấn.
            </p>
            <div class="status-badge">● System Online: Secure Connection</div>
        </div>
    """, unsafe_allow_html=True)

    # AVATAR SECTION
    col1, col2, col3 = st.columns([1, 8, 1])
    with col2:
        # height=550 là chuẩn cho desktop làm việc văn phòng
        components.html(get_heygen_html_snippet(), height=550, scrolling=False)

if __name__ == "__main__":
    main()