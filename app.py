import streamlit as st
import streamlit.components.v1 as components

# --- 1. SETUP PAGE ---
st.set_page_config(
    page_title="HeyGen AI Space Core",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. DEEP SPACE UI & PARTICLE SYSTEM ---
def inject_space_css():
    st.markdown("""
        <style>
            /* IMPORT FONT */
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Exo+2:wght@300;600&display=swap');

            /* --- BACKGROUND: DEEP SPACE LAYERS --- */
            .stApp {
                background-color: #000;
                /* Lớp 1: Sao nhỏ li ti */
                background-image: 
                    radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
                    radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
                    radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 20px),
                    /* Lớp 2: Tinh vân màu tối tạo chiều sâu */
                    radial-gradient(circle at 50% 50%, rgba(20, 30, 50, 0.4) 0%, rgba(0,0,0,0) 70%);
                background-size: 550px 550px, 350px 350px, 250px 250px, 100% 100%;
                background-position: 0 0, 40px 60px, 130px 270px, center;
                animation: spaceMove 120s linear infinite; /* Vũ trụ di chuyển chậm */
            }
            
            @keyframes spaceMove {
                from { background-position: 0 0, 40px 60px, 130px 270px, center; }
                to { background-position: 550px 550px, 390px 410px, 380px 520px, center; }
            }

            /* --- CANVAS CHO HIỆU ỨNG VỆT SAO --- */
            #particle-canvas {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none; /* Quan trọng: để không chặn click chuột */
                z-index: 1; /* Nằm trên nền nhưng dưới các nút bấm */
                mix-blend-mode: screen; /* Hòa trộn ánh sáng */
            }

            /* ẨN UI THỪA */
            #MainMenu, footer, header {visibility: hidden;}
            .block-container { padding-top: 2rem; padding-bottom: 0rem; max-width: 100%; }

            /* TYPOGRAPHY SPACE STYLE */
            .space-title {
                font-family: 'Orbitron', sans-serif;
                text-align: center;
                font-size: 3rem;
                font-weight: 700;
                background: linear-gradient(to bottom, #fff, #87ceeb);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0 0 20px rgba(135, 206, 235, 0.8);
                letter-spacing: 6px;
                margin-bottom: 10px;
            }

            .space-subtitle {
                font-family: 'Exo 2', sans-serif;
                text-align: center;
                color: #aaddff;
                font-size: 1rem;
                letter-spacing: 2px;
                opacity: 0.8;
            }
        </style>
        
        <canvas id="particle-canvas"></canvas>
        <script>
            const canvas = document.getElementById('particle-canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            let particlesArray = [];
            const colors = ['#ffffff', '#87ceeb', '#e0ffff', '#b0e0e6']; // Màu bụi sao

            window.addEventListener('resize', function(){
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            });

            const mouse = { x: undefined, y: undefined };
            window.addEventListener('mousemove', function(event){
                mouse.x = event.x;
                mouse.y = event.y;
                // Tạo ra nhiều hạt mỗi khi chuột di chuyển
                for (let i = 0; i < 3; i++) {
                    particlesArray.push(new Particle());
                }
            });

            class Particle {
                constructor(){
                    this.x = mouse.x;
                    this.y = mouse.y;
                    // Kích thước ngẫu nhiên
                    this.size = Math.random() * 3 + 1;
                    // Tốc độ và góc di chuyển ngẫu nhiên (tạo hiệu ứng nổ nhẹ)
                    this.speedX = Math.random() * 2 - 1;
                    this.speedY = Math.random() * 2 - 1;
                    this.color = colors[Math.floor(Math.random() * colors.length)];
                    this.life = 1.0; // Độ trong suốt (thời gian sống)
                }
                update(){
                    this.x += this.speedX;
                    this.y += this.speedY;
                    // Giảm kích thước và độ trong suốt theo thời gian
                    if (this.size > 0.2) this.size -= 0.05;
                    this.life -= 0.02;
                }
                draw(){
                    ctx.fillStyle = this.color;
                    ctx.globalAlpha = this.life; // Áp dụng độ trong suốt
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.globalAlpha = 1.0; // Reset
                }
            }

            function handleParticles(){
                for (let i = 0; i < particlesArray.length; i++){
                    particlesArray[i].update();
                    particlesArray[i].draw();
                    // Xóa hạt khi nó quá nhỏ hoặc hết thời gian sống
                    if (particlesArray[i].size <= 0.3 || particlesArray[i].life <= 0){
                        particlesArray.splice(i, 1);
                        i--;
                    }
                }
            }

            function animate(){
                // Tạo hiệu ứng vệt mờ bằng cách xóa khung hình không hoàn toàn
                ctx.fillStyle = 'rgba(0,0,0,0.1)'; 
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                handleParticles();
                requestAnimationFrame(animate);
            }
            animate();
        </script>
    """, unsafe_allow_html=True)

# --- 3. HEYGEN COMPONENT (FIXED CROP & SPACE STYLE) ---
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
              
              /* --- SỬA LỖI CẮT ẢNH (CROP FIX) --- */
              width: 150px; height: 150px; /* Đảm bảo là hình vuông tuyệt đối */
              border-radius: 50%; /* Biến hình vuông thành hình tròn */
              overflow: hidden; /* Cắt bỏ phần thừa */
              
              /* Căn chỉnh ảnh nền chuẩn xác */
              background-image: url('https://files2.heygen.ai/avatar/v3/74447a27859a456c955e01f21ef18216_45620/preview_talk_1.webp');
              background-size: cover; /* Ảnh phủ kín khung tròn mà không bị méo */
              background-position: center 20%; /* Ưu tiên hiển thị khuôn mặt */
              background-repeat: no-repeat;

              /* Hiệu ứng viền vũ trụ */
              border: 3px solid rgba(135, 206, 235, 0.5);
              box-shadow: 0 0 40px rgba(135, 206, 235, 0.4), inset 0 0 20px rgba(255,255,255,0.2);
              
              transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); /* Hiệu ứng nảy nhẹ */
              opacity: 0; visibility: hidden;
              cursor: pointer;
          }
          
          /* Hiệu ứng khi di chuột vào nút */
          #heygen-streaming-embed:hover {
              transform: translate(-50%, -50%) scale(1.1);
              box-shadow: 0 0 60px rgba(135, 206, 235, 0.8), inset 0 0 30px rgba(255,255,255,0.4);
              border-color: rgba(255, 255, 255, 0.8);
          }

          #heygen-streaming-embed.show { opacity: 1; visibility: visible; }

          /* KHI MỞ RỘNG */
          #heygen-streaming-embed.expand {
              width: 100%; height: 100%;
              max-width: 800px;
              border-radius: 12px;
              border: 1px solid rgba(135, 206, 235, 0.3);
              box-shadow: 0 20px 60px rgba(0,0,0,0.8);
              background: #000;
              /* Khi mở rộng thì bỏ ảnh nền đi */
              background-image: none; 
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
    inject_space_css()

    # Header Section
    st.markdown('<div class="space-title">GALACTIC AI INTERFACE</div>', unsafe_allow_html=True)
    st.markdown('<div class="space-subtitle">SYSTEM ONLINE | INITIALIZING NEURAL LINK...</div>', unsafe_allow_html=True)

    # Avatar Section
    col1, col2, col3 = st.columns([1, 10, 1])
    with col2:
        # Giữ chiều cao compact
        components.html(get_heygen_html_snippet(), height=520, scrolling=False)

if __name__ == "__main__":
    main()