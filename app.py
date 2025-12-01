import streamlit as st
import streamlit.components.v1 as components
import textwrap # Thư viện để xử lý lỗi thụt dòng văn bản

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Audit Intelligence Workspace",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS (FIXED LAYOUT) ---
def inject_dashboard_css():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@700&display=swap');

            :root {
                --primary-color: #0F172A;
                --accent-color: #3B82F6;
                --bg-color: #F8FAFC;
                --card-bg: #FFFFFF;
            }

            .stApp {
                background-color: var(--bg-color);
                font-family: 'Inter', sans-serif;
            }

            #MainMenu, footer, header {visibility: hidden;}
            .block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1400px; }

            /* --- HEADER --- */
            .header-container {
                display: flex; justify-content: space-between; align-items: center;
                margin-bottom: 30px; border-bottom: 2px solid #E2E8F0; padding-bottom: 15px;
            }
            .app-title {
                font-family: 'Playfair Display', serif; font-size: 1.8rem;
                color: var(--primary-color); font-weight: 700;
            }
            .app-badge {
                background: #DBEAFE; color: #1E40AF; padding: 5px 12px;
                border-radius: 20px; font-size: 0.8rem; font-weight: 600;
            }

            /* --- CARDS --- */
            /* Quan trọng: CSS cho thẻ HTML bên trái */
            .welcome-box {
                background: var(--card-bg);
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.05);
                border-left: 5px solid var(--accent-color);
            }
            .welcome-title {
                font-size: 1.4rem; font-weight: 600; color: var(--primary-color); margin-bottom: 8px;
            }
            
            /* --- GRID --- */
            .quick-actions-grid {
                display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 20px;
            }
            .action-card {
                background: #fff; border: 1px solid #E2E8F0; padding: 15px;
                border-radius: 8px; cursor: pointer; transition: all 0.2s;
            }
            .action-card:hover {
                border-color: var(--accent-color); transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            }
            .action-title { font-weight: 600; color: var(--primary-color); display: block; font-size: 0.95rem; }
            .action-desc { font-size: 0.8rem; color: #64748B; margin-top: 4px; display: block; }

        </style>
    """, unsafe_allow_html=True)

# --- 3. HEYGEN COMPONENT (CLEAN VERSION) ---
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
        body { display: flex; justify-content: center; align-items: flex-start; } /* Căn lên trên cùng */
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
              top: 50px; /* Đẩy xuống một chút để đẹp hơn */
              left: 50%;
              transform: translateX(-50%);
              
              width: 170px; height: 170px;
              border-radius: 50%;
              overflow: hidden; 
              
              background-image: url('https://files2.heygen.ai/avatar/v3/74447a27859a456c955e01f21ef18216_45620/preview_talk_1.webp');
              background-size: cover;
              background-position: center 20%;
              
              border: 4px solid #fff;
              box-shadow: 0 10px 30px rgba(0,0,0,0.15);
              
              transition: all 0.4s ease;
              opacity: 0; visibility: hidden;
              cursor: pointer;
          }

          #heygen-streaming-embed:hover {
              transform: translateX(-50%) scale(1.05);
              box-shadow: 0 15px 40px rgba(59, 130, 246, 0.3);
              border-color: #EFF6FF;
          }

          #heygen-streaming-embed.expand {
              width: 100% !important; 
              height: 100% !important;
              max-width: 100% !important;
              border-radius: 0;
              border: none;
              box-shadow: none;
              background: transparent; 
              top: 0; left: 0;
              transform: none;
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

# --- 4. RENDER UI ---
def render_header():
    st.markdown("""
        <div class="header-container">
            <div class="app-title">Audit Intelligence Suite</div>
            <div class="app-badge">Enterprise Edition v2.1</div>
        </div>
    """, unsafe_allow_html=True)

def render_welcome_card():
    # SỬ DỤNG TEXTWRAP.DEDENT ĐỂ XÓA KHOẢNG TRẮNG THỪA
    # Đảm bảo HTML không bị hiểu nhầm là Code block
    html_content = textwrap.dedent("""
        <div class="welcome-box">
            <div class="welcome-title">Xin chào, Kiểm toán viên.</div>
            <div style="color: #64748B; margin-bottom: 20px; line-height: 1.5;">
                Hệ thống AI đã sẵn sàng. Bạn muốn bắt đầu từ đâu? 
                Chọn tác vụ nhanh bên dưới hoặc kích hoạt <strong>Trợ lý ảo</strong>.
            </div>
            
            <div class="quick-actions-grid">
                <div class="action-card">
                    <span class="action-title">📊 Phân tích Báo cáo</span>
                    <span class="action-desc">Rà soát BCTC & Dòng tiền</span>
                </div>
                <div class="action-card">
                    <span class="action-title">🛡️ Đánh giá Rủi ro</span>
                    <span class="action-desc">Kiểm tra tuân thủ & Gian lận</span>
                </div>
                <div class="action-card">
                    <span class="action-title">📑 Tra cứu Luật</span>
                    <span class="action-desc">Quy định VAS & IFRS</span>
                </div>
                <div class="action-card">
                    <span class="action-title">✍️ Soạn thảo Email</span>
                    <span class="action-desc">Yêu cầu hồ sơ khách hàng</span>
                </div>
            </div>
        </div>
    """)
    st.markdown(html_content, unsafe_allow_html=True)

# --- 5. MAIN APP ---
def main():
    inject_dashboard_css()
    render_header()

    col_content, col_avatar = st.columns([1.5, 1])

    with col_content:
        render_welcome_card()
        st.info("💡 **Gợi ý:** Có 3 bút toán cần chú ý tại sổ cái tài khoản 642.")

    with col_avatar:
        # Đã xóa div wrapper gây lỗi layout
        # Giờ đây component sẽ tự căn chỉnh đẹp mắt
        components.html(get_heygen_html_snippet(), height=550, scrolling=False)

if __name__ == "__main__":
    main()