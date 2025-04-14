# -*- coding: utf-8 -*-
import os
import sys
import time
import logging
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import WebDriverException

# 配置日志记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('selenium.log')
    ]
)
logger = logging.getLogger(__name__)

# 配置Edge浏览器选项
def configure_edge_options():
    options = Options()
    
    # 无头模式 + 服务器兼容性配置
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # 反自动化检测
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    
    # 用户代理和SSL设置
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")
    
    return options

# 安全加载网页函数
def safe_get(driver, url, max_retries=3, delay=5):
    for attempt in range(max_retries):
        try:
            logger.info(f"尝试 {attempt + 1}/{max_retries}: 加载 {url}")
            driver.get(url)
            time.sleep(2)
            return True
        except WebDriverException as e:
            logger.error(f"加载失败: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(delay)
    return False

# JavaScript颜色查找函数
find_element_by_color_script = """
function findElementByColor(color) {
    const elements = document.querySelectorAll('*');
    for (let element of elements) {
        const bgColor = window.getComputedStyle(element).backgroundColor;
        if (bgColor === color) {
            return element;
        }
    }
    return null;
}
return findElementByColor(arguments[0]);
"""

# 主函数
def main():
    try:
        # 初始化浏览器
        options = configure_edge_options()
        
        # 自动安装WebDriver（兼容GitHub Actions环境）
        try:
            from webdriver_manager.microsoft import EdgeChromiumDriverManager
            service = Service(EdgeChromiumDriverManager().install())
        except Exception as e:
            logger.warning(f"WebDriver自动安装失败: {e}, 尝试使用系统路径")
            service = Service('/usr/bin/msedgedriver')  # GitHub Actions默认路径
        
        driver = webdriver.Edge(service=service, options=options)
        driver.set_window_size(1200, 800)
        
        # 网页列表（示例，实际可替换为你的URL列表）
        urls = [
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003723842&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003724018&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003724350&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003724476&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003725760&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003726260&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003726291&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003726315&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003726386&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003726475&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003728704&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003729339&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003729441&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003728212&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003727686&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003727207&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003726989&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003726428&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=5003710382&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41805054&id=41805054&key=01jhgnstr21se9mrycz2tpgbp1#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000348087&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000348191&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000348259&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000347958&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=41340931&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000349675&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000356673&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000361748&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000367577&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000369601&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000380585&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000380637&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000389530&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000389596&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000397000&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000461507&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000457954&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000457902&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000434065&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=5000433853&key=01j0g6mx3ryjmqabscs058mpq2#/",
    "http://47.76.150.147:8888/?ch=vx&uid=41340931&id=41340931&key=01j0g6mx3ryjmqabscs058mpq2#/"
        ]
        
        # 主循环
        for url in urls:
            logger.info(f"处理URL: {url}")
            if not safe_get(driver, url):
                logger.error(f"跳过无法加载的URL: {url}")
                continue
            
            try:
                # 查找并点击绿色元素
                green_color = "rgb(76, 175, 80)"
                element = driver.execute_script(find_element_by_color_script, green_color)
                if element:
                    element.click()
                    logger.info("成功点击绿色元素")
                else:
                    logger.warning("未找到绿色元素")
            except Exception as e:
                logger.error(f"执行操作时出错: {e}")
            
            time.sleep(15)  # 页面间间隔
        
    except Exception as e:
        logger.critical(f"程序崩溃: {e}", exc_info=True)
    finally:
        if 'driver' in locals():
            driver.quit()
        logger.info("浏览器已关闭")

if __name__ == "__main__":
    logger.info("===== 脚本开始运行 =====")
    main()
    logger.info("===== 脚本运行结束 =====")
