import streamlit as st
import streamlit.components.v1 as components

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Audit Intelligence Workspace",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. ADVANCED CSS (DASHBOARD STYLE) ---
def inject_dashboard_css():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@700&display=swap');

            :root {
                --primary-color: #0F172A; /* Slate 900 */
                --accent-color: #3B82F6;  /* Blue 500 */
                --bg-color: #F8FAFC;      /* Slate 50 */
                --card-bg: #FFFFFF;
                --text-main: #334155;
            }

            .stApp {
                background-color: var(--bg-color);
                font-family: 'Inter', sans-serif;
            }

            /* HIDE DEFAULT ELEMENTS */
            #MainMenu, footer, header {visibility: hidden;}
            .block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1400px; }

            /* --- HEADER --- */
            .header-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 40px;
                border-bottom: 2px solid #E2E8F0;
                padding-bottom: 20px;
            }
            .app-title {
                font-family: 'Playfair Display', serif;
                font-size: 2rem;
                color: var(--primary-color);
                font-weight: 700;
                letter-spacing: -0.5px;
            }
            .app-badge {
                background: #DBEAFE;
                color: #1E40AF;
                padding: 6px 16px;
                border-radius: 20px;
                font-size: 0.85rem;
                font-weight: 600;
            }

            /* --- ACTION CARDS (LEFT SIDE) --- */
            .welcome-box {
                background: var(--card-bg);
                padding: 30px;
                border-radius: 16px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
                border-left: 6px solid var(--accent-color);
            }
            .welcome-title {
                font-size: 1.5rem;
                font-weight: 600;
                color: var(--primary-color);
                margin-bottom: 10px;
            }
            .welcome-text {
                color: #64748B;
                line-height: 1.6;
            }

            /* --- QUICK ACTIONS GRID --- */
            .quick-actions-grid {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 15px;
                margin-top: 20px;
            }
            .action-card {
                background: white;
                border: 1px solid #E2E8F0;
                padding: 20px;
                border-radius: 12px;
                cursor: pointer;
                transition: all 0.2s;
                text-align: left;
            }
            .action-card:hover {
                border-color: var(--accent-color);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
                transform: translateY(-2px);
            }
            .action-icon { font-size: 1.5rem; margin-bottom: 10px; display: block; }
            .action-title { font-weight: 600; color: var(--primary-color); display: block; }
            .action-desc { font-size: 0.85rem; color: #94A3B8; margin-top: 5px; display: block; }

            /* --- AVATAR CONTAINER (RIGHT SIDE) --- */
            .avatar-wrapper {
                background: #FFFFFF;
                border-radius: 24px;
                padding: 10px;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
                border: 1px solid #F1F5F9;
                height: 520px; /* Chiều cao cố định để cân đối layout */
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                overflow: hidden;
            }
            
            /* Label nhỏ trên avatar */
            .ai-status {
                position: absolute;
                top: 20px;
                right: 20px;
                background: rgba(16, 185, 129, 0.1);
                color: #059669;
                padding: 4px 12px;
                border-radius: 12px;
                font-size: 0.75rem;
                font-weight: 700;
                z-index: 10;
                backdrop-filter: blur(4px);
            }

        </style>
    """, unsafe_allow_html=True)

# --- 3. HEYGEN COMPONENT (FITTED) ---
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
              
              /* Viền tạo cảm giác chuyên nghiệp */
              border: 4px solid #fff;
              box-shadow: 0 10px 25px rgba(0,0,0,0.1);
              
              transition: all 0.4s ease;
              opacity: 0; visibility: hidden;
              cursor: pointer;
          }

          #heygen-streaming-embed:hover {
              transform: translate(-50%, -50%) scale(1.05);
              box-shadow: 0 15px 35px rgba(59, 130, 246, 0.2); /* Blue shadow */
              border-color: #EFF6FF;
          }

          /* KHI MỞ RỘNG - VỪA KHÍT KHUNG BÊN PHẢI */
          #heygen-streaming-embed.expand {
              width: 100% !important; 
              height: 100% !important;
              max-width: 100% !important;
              max-height: 100% !important;
              border-radius: 0;
              border: none;
              box-shadow: none;
              background: transparent; 
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

# --- 4. UI HELPER FUNCTIONS ---
def render_header():
    st.markdown("""
        <div class="header-container">
            <div class="app-title">Audit Intelligence Suite</div>
            <div class="app-badge">Enterprise Edition v2.0</div>
        </div>
    """, unsafe_allow_html=True)

def render_welcome_card():
    st.markdown("""
        <div class="welcome-box">
            <div class="welcome-title">Xin chào, Kiểm toán viên.</div>
            <div class="welcome-text">
                Hệ thống AI đã sẵn sàng hỗ trợ. Dữ liệu tài chính Q4 đã được đồng bộ. 
                Bạn muốn bắt đầu từ đâu? Hãy chọn một tác vụ nhanh hoặc kích hoạt 
                <strong>Trợ lý ảo</strong> bên tay phải để hội thoại trực tiếp.
            </div>
            
            <div class="quick-actions-grid">
                <div class="action-card">
                    <span class="action-icon">📊</span>
                    <span class="action-title">Phân tích Báo cáo</span>
                    <span class="action-desc">Rà soát BCTC & Lưu chuyển tiền tệ</span>
                </div>
                <div class="action-card">
                    <span class="action-icon">🛡️</span>
                    <span class="action-title">Đánh giá Rủi ro</span>
                    <span class="action-desc">Kiểm tra tuân thủ & Gian lận</span>
                </div>
                <div class="action-card">
                    <span class="action-icon">📑</span>
                    <span class="action-title">Tra cứu Luật</span>
                    <span class="action-desc">Quy định VAS & IFRS mới nhất</span>
                </div>
                <div class="action-card">
                    <span class="action-icon">✍️</span>
                    <span class="action-title">Soạn thảo Email</span>
                    <span class="action-desc">Gửi yêu cầu cung cấp hồ sơ</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- 5. MAIN APP LAYOUT ---
def main():
    inject_dashboard_css()
    render_header()

    # Layout chia cột: 60% Nội dung - 40% Avatar
    # Giúp giao diện cân đối, người dùng vừa làm việc vừa chat được
    col_content, col_avatar = st.columns([1.4, 1])

    with col_content:
        render_welcome_card()
        # Mockup một biểu đồ nhỏ hoặc log để trông giống Dashboard thật
        st.info("💡 Gợi ý: Hôm nay có 3 bút toán cần chú ý tại sổ cái tài khoản 642.")

    with col_avatar:
        # Avatar được bọc trong một container riêng biệt, đẹp mắt
        st.markdown('<div class="avatar-wrapper">', unsafe_allow_html=True)
        st.markdown('<div class="ai-status">● LIVE</div>', unsafe_allow_html=True)
        # height 500px là vừa đủ để fit vào khung bên phải
        components.html(get_heygen_html_snippet(), height=500, scrolling=False)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()