from app.core.database import db
from app.models.category_model import CategoryModel
from app.models.product_model import ProductModel

products = [
    {
        "model": "Processador AMD Ryzen 5 3600, AM4, 3.6GHz",
        "img": "https://static.meupc.net/produto/processador-amd-ryzen-5-3600-100100000031box-jXdm89-L.jpg",
        "price": 1678.31,
        "description": "Marca: AMD, Modelo: Ryzen 5 3600, Cores: 6, Threads: 12, Socket: AM4, Base Clock: 3.6, Cooler Box: Incluso, GPU Integrada: Não, Consumo: 65 Watts",
        "category": "Processador",
    },
    {
        "model": "Processador AMD Ryzen 7 5800X, AM4, 3.8GHz",
        "img": "https://static.meupc.net/produto/processador-amd-ryzen-7-5800x-100100000063wof-g3T5mn-L.jpg",
        "price": 2599.9,
        "description": "Marca: AMD, Modelo: Ryzen 7 5800X, Cores: 8, Threads: 16, Socket: AM4, Base Clock: 3.8, Cooler Box: Incluso, GPU Integrada: Não, Consumo: 105 Watts",
        "category": "Processador",
    },
    {
        "model": "Processador AMD Ryzen 9 5900X, AM4, 3.7 GHz",
        "img": "https://static.meupc.net/produto/processador-amd-ryzen-9-5900x-100100000061wof-Bjt4U3-L.jpg",
        "price": 2599.9,
        "description": "Marca: AMD, Modelo: Ryzen 9 5900X, Cores: 12, Threads: 24, Socket: AM4, Base Clock: 3.7, Cooler Box: Incluso, GPU Integrada: Não, Consumo: 105 Watts",
        "category": "Processador",
    },
    {
        "model": "Processador Intel Core i3-10100F, LGA 1200, 3.6 GHz",
        "img": "https://static.meupc.net/produto/processador-intel-core-i3-10100f-bx8070110100f-CTk878-L.jpg",
        "price": 657.46,
        "description": "Marca: Intel, Modelo: Core i3-10100F, Cores: 4, Threads: 8, Socket: LGA 1200, Base Clock: 3.6, Cooler Box: Incluso, GPU Integrada: Não, Consumo: 65 Watts",
        "category": "Processador",
    },
    {
        "model": "Processador Intel Core i3-10100, LGA 1200, 3.6 GHz",
        "img": "https://static.meupc.net/produto/processador-intel-core-i3-10100f-bx8070110100f-CTk878-L.jpg",
        "price": 897.9,
        "description": "Marca: Intel, Modelo: Core i3-10100, Cores: 4, Threads: 8, Socket: LGA 1200, Base Clock: 3.6, Cooler Box: Incluso, GPU Integrada: UHD Graphics 630, Consumo: 65 Watts",
        "category": "Processador",
    },
    {
        "model": "Processador Intel Core i5-11600K, LGA 1200, 3.9 GHz",
        "img": "https://static.meupc.net/produto/processador-intel-core-i5-11600k-bx8070811600k-ATXe46-L.jpg",
        "price": 1799.99,
        "description": "Marca: Intel, Modelo: Core i5-11600K, Cores: 8, Threads: 12, Socket: LGA 1200, Base Clock: 3.9, Cooler Box: Incluso, GPU Integrada: UHD Graphics 730, Consumo: 125 Watts",
        "category": "Processador",
    },
    {
        "model": "Processador Intel Core i7-11700K, LGA 1200, 3.6 GHz",
        "img": "https://static.meupc.net/produto/processador-intel-core-i7-11700k-bx8070811700k-dHBH99-L.jpg",
        "price": 2749.31,
        "description": "Marca: Intel, Modelo: Core i5-11700K, Cores: 8, Threads: 12, Socket: LGA 1200, Base Clock: 3.9, Cooler Box: Incluso, GPU Integrada: UHD Graphics 730, Consumo: 125 Watts",
        "category": "Processador",
    },
    {
        "model": "Processador Intel Core i7-9700K, LGA 1151, 3.6 GHz 8-Core",
        "img": "https://static.meupc.net/produto/processador-intel-core-i7-11700k-bx8070811700k-dHBH99-L.jpg",
        "price": 2749.31,
        "description": "Marca: Intel, Modelo: Core i7-9700K, Cores: 8, Threads: 8, Socket: LGA 1151, Base Clock: 3.6, Cooler Box: Não, GPU Integrada: UHD Graphics 730, Consumo: 95 Watts",
        "category": "Processador",
    },
    {
        "model": "Processador Intel Core i9-11900K, LGA 1200, 3.5 GHz",
        "img": "https://static.meupc.net/produto/processador-intel-core-i9-11900k-bx8070811900k-sX5Lj2-L.jpg",
        "price": 5016.88,
        "description": "Marca: Intel, Modelo: Core i9-11900K, Cores: 10, Threads: 20, Socket: LGA 1200, Base Clock: 3.7, Cooler Box: Não, GPU Integrada: UHD Graphics 750, Consumo: 125 Watts",
        "category": "Processador",
    },
    {
        "model": "Cooler para Processador Scythe Ninja 5, Intel/AMD",
        "img": "https://static.meupc.net/produto/cooler-processador-scythe-ninja-5-vL48Js-L.jpg",
        "price": 399.99,
        "description": "Marca: Scythe, Modelo: SCNJ-5000, Socket compatíveis: AM4 | LGA1156 | LGA1200 | LGA1366, Velocidade do ventilador: 300 ~ 800rpm",
        "category": "Cooler",
    },
    {
        "model": "Cooler de processador PCYes Nótus A Hidráulico",
        "img": "https://static.meupc.net/produto/cooler-processador-pcyes-notus-a-qoy442-L.jpg",
        "price": 80.89,
        "description": "Marca: PCYes, Modelo: Nótus A, Socket compatíveis: AM4 | FM1 | AM3 | AM2, Velocidade do ventilador: 500 ~ 1800rpm",
        "category": "Cooler",
    },
    {
        "model": "Cooler de processador Cooler Master Hyper H411R Fluido Dinâmico",
        "img": "https://static.meupc.net/produto/cooler-processador-cooler-master-hyper-h411r-ir5Ew2-L.jpg",
        "price": 249.99,
        "description": "Marca: Cooler Maste, Modelo: RR-H411-20PW-R1, Socket compatíveis: AM4 | LGA1156 | LGA1200 | LGA1366, Velocidade do ventilador: 600 ~ 2000rpm",
        "category": "Cooler",
    },
    {
        "model": "Cooler de processador Thermaltake Frio Extreme CLP0587",
        "img": "https://static.meupc.net/produto/cooler-processador-thermaltake-frio-extreme-clp0587-xG3I7r-L.jpg",
        "price": 1069.37,
        "description": "Marca: Thermaltake, Modelo: CLP0587, Socket compatíveis: AM4 | LGA1156 | LGA1200 | LGA1366, Velocidade do ventilador: 600 ~ 2000rpm",
        "category": "Cooler",
    },
    {
        "model": "Water Cooler Deepcool Gammaxx L120 V2 RGB",
        "img": "https://static.meupc.net/produto/cooler-processador-deepcool-gammaxx-l120-v2-Bz9n9S-L.jpg",
        "price": 406.8,
        "description": "Marca: Deepcool, Modelo: Gammaxx L120 V2 RGB, Socket compatíveis: AM4 | LGA1156 | LGA1200 | LGA1366, Velocidade do ventilador: 600 ~ 2000rpm",
        "category": "Cooler",
    },
    {
        "model": "Water Cooler Thermaltake Water 3.0 Riing RGB 280",
        "img": "https://static.meupc.net/produto/cooler-processador-cooler-master-hyper-h411r-ir5Ew2-L.jpg",
        "price": 1644.54,
        "description": "Marca: Thermaltake, Modelo: CL-W138-PL14SW-A, Socket compatíveis: AM4 | LGA1156 | LGA1200 | LGA1366, Velocidade do ventilador: 800 ~ 1500rpm",
        "category": "Cooler",
    },
    {
        "model": "Placa de Vídeo Zotac NVIDIA GeForce RTX 2060, 6GB, GDDR6",
        "img": "https://static.meupc.net/produto/placa-video-zotac-geforce-rtx-2060-geforcertx2060gaming6gb-xm5w2F-L.jpg",
        "price": 4235.18,
        "description": "Marca: Zotac, Modelo: RTX 2060 6GB, CUDA Cores: 1920, Saídas de Vídeo: 3x DisplayPort e 1x HDMI, Memória: GDDR6 6GB e 14000MHz, Fonte recomendada: 500W",
        "category": "Placa de Video",
    },
    {
        "model": "Placa de Vídeo Gainward NVIDIA GeForce GTX 1650, 4GB D6 Ghost, GDDR6",
        "img": "https://static.meupc.net/produto/placa-video-gainward-geforce-gtx-1650-geforcegtx1650ghost4gb-xts49r-L.jpg",
        "price": 2362.2,
        "description": "Marca: Gainward, Modelo: GTX 1650 4GB, CUDA Cores: 869, Saídas de Vídeo: 2x DisplayPort e 1x HDMI, Memória: GDDR6 4GB e 6000MHz, Fonte recomendada: 300W",
        "category": "Placa de Video",
    },
    {
        "model": "Placa de Vídeo Asus NVIDIA GeForce RTX 3090, 24GB, GDDR6X ROG STRIX GAMING",
        "img": "https://images.kabum.com.br/produtos/fotos/163879/placa-de-video-asus-rog-strix-rtx-3070-ti-o8g-gaming-19-gbps-8gb-gddr6x-ray-tracing-dlss-rgb-90yv0gw0-m0na00_1623333955_gg.jpg",
        "price": 30689.07,
        "description": "Marca: Asus, Modelo: RTX 3090 24GB, CUDA Cores: 10496, Saídas de Vídeo: 3x DisplayPort e 2x HDMI, Memória: GDDR6 24GB e 19500MHz, Fonte recomendada: 300W",
        "category": "Placa de Video",
    },
    {
        "model": "Placa de Vídeo PowerColor AMD Radeon RX 570, 4GB GDDR5",
        "img": "https://static.meupc.net/produto/placa-video-powercolor-radeon-rx-570-radeonrx5704gb-DAR334-L.jpg",
        "price": 4863.9,
        "description": "Marca: PowerColor, Modelo: RX 570 4GB, CUDA Cores: 2304, Saídas de Vídeo: 3x DisplayPort e 2x HDMI + 1x DVI-D, Memória: GDDR5 4GB e 7000MHz, Fonte recomendada: 500W",
        "category": "Placa de Video",
    },
    {
        "model": "Placa de Vídeo Asus TUF GAMING, AMD Radeon RX 6900 XT, 16GB, GDDR6",
        "img": "https://static.meupc.net/produto/placa-video-asus-radeon-rx-6900-xt-tufgamingradeonrx6900xt16gb-s64ojq-L.jpg",
        "price": 14117.53,
        "description": "Marca: Asus, Modelo: RX 6900 XT 16GB, CUDA Cores: 5120, Saídas de Vídeo: 3x DisplayPort e 1x HDMI, Memória: GDDR6 16GB e 16000MHz, Fonte recomendada: 850W",
        "category": "Placa de Video",
    },
    {
        "model": "Placa de Vídeo PowerColor Red Devil AMD Radeon RX 6700 XT, 12GB, GDDR6",
        "img": "https://static.meupc.net/produto/placa-video-powercolor-radeon-rx-6700-xt-radeonrx6700xtreddevil12gb-o6DXj4-L.jpg",
        "price": 9029.9,
        "description": "Marca: PowerColor, Modelo: RX 6700 XT 12GB, CUDA Cores: 2560, Saídas de Vídeo: 3x DisplayPort e 1x HDMI, Memória: GDDR6 12GB e 16000MHz, Fonte recomendada: 700W",
        "category": "Placa de Video",
    },
    {
        "model": "Placa Mãe Asus PRIME Z590-PLUS, Intel LGA1200, ATX, DDR4",
        "img": "https://static.meupc.net/produto/placa-mae-asus-prime-z590m-plus-jYd44z-L.jpg",
        "price": 1646.94,
        "description": "Marca: Asus, Modelo: PRIME Z590-PLUS, Socket: LGA 1200, Memória Máxima: 128GB, Slots de memória: 4, Técnologia: DDR4, Slots PCI-E 16x: 2, Entradas Sata: 5, Entradas M2: 3, Entradas USB: 8",
        "category": "Placa de Video",
    },
    {
        "model": "Placa Mãe Gigabyte B550M Aorus Elite AMD AM4, mATX, DDR4",
        "img": "https://static.meupc.net/produto/placa-mae-gigabyte-b550m-aorus-elite-bZd7k5-L.jpg",
        "price": 1046.94,
        "description": "Marca: Gigabyte, Modelo: B550M Aorus Elite, Socket: AM4, Memória Máxima: 128GB, Slots de memória: 4, Técnologia: DDR4, Slots PCI-E 16x: 2, Entradas Sata: 4, Entradas M2: 2, Entradas USB: 8",
        "category": "Placa Mae",
    },
    {
        "model": "Placa Mãe Asus ROG Strix X570-E Gaming, AM4, ATX, DDR4",
        "img": "https://static.meupc.net/produto/placa-mae-asus-rog-strix-x570-e-gaming-km49AQ-L.jpg",
        "price": 3170.13,
        "description": "Marca: Asus, Modelo: ROG Strix X570-E Gaming, Socket: AM4, Memória Máxima: 128GB, Slots de memória: 4, Técnologia: DDR4, Slots PCI-E 16x: 3, Entradas Sata: 8, Entradas M2: 1, Entradas USB: 6",
        "category": "Placa Mae",
    },
    {
        "model": "Placa Mãe Gigabyte Z390 M Gaming, Intel LGA1151, mATX, DDR4",
        "img": "https://static.meupc.net/produto/placa-mae-asrock-z390-m-gaming-o9Ny5u-L.jpg",
        "price": 1258.71,
        "description": "Marca: Gigabyte, Modelo: Z390 M Gaming, Socket: LGA 1151, Memória Máxima: 64GB, Slots de memória: 4, Técnologia: DDR4, Slots PCI-E 16x: 2, Entradas Sata: 6, Entradas M2: 2, Entradas USB: 5",
        "category": "Placa Mae",
    },
    {
        "model": "Placa-mãe Asus Prime B450M Gaming/BR Micro ATX, AM4 B450, DDR4",
        "img": "https://static.meupc.net/produto/placa-mae-asus-prime-b450m-gaming-wv2v34-L.jpg",
        "price": 529.9,
        "description": "Marca: Asus, Modelo: B450M Gaming/BR, Socket: AM4, Memória Máxima: 64GB, Slots de memória: 4, Técnologia: DDR4, Slots PCI-E 16x: 1, Entradas Sata: 4, Entradas M2: 1, Entradas USB: 6",
        "category": "Placa Mae",
    },
    {
        "model": "Placa-mãe MSI MEG Z490 ACE, Intel LGA1200, ATX, DDR4",
        "img": "https://static.meupc.net/produto/placa-mae-msi-meg-z490-ace-pXzx38-L.jpg",
        "price": 2997.9,
        "description": "Marca: MSI, Modelo: MEG Z490 ACE, Socket: LGA1200, Memória Máxima: 128GB, Slots de memória: 4, Técnologia: DDR4, Slots PCI-E 16x: 3, Entradas Sata: 6, Entradas M2: 4, Entradas USB: 8",
        "category": "Placa Mae",
    },
    {
        "model": "Memória Crucial Ballistix 8GB DDR4 2666MHz",
        "img": "https://images.kabum.com.br/produtos/fotos/135291/memoria-ram-crucial-ballistix-8gb-ddr4-2666-mhz-cl16-udimm-preto-bl8g26c16u4b_1609871709_gg.jpg",
        "price": 305.76,
        "description": "Marca: MSI, Modelo: MEG Z490 ACE, Clock: 2666Mhz, Capacidade: 8GB, Tecnologia: DDR4",
        "category": "Memoria RAM",
    },
    {
        "model": "Memória Corsair Vengeance RGB Pro 8GB DDR4 3200MHz",
        "img": "https://static.meupc.net/produto/memoria-corsair-vengeance-pro-cmw8gx4m1z3200c16-jVap79-L.jpg",
        "price": 541.06,
        "description": "Marca: Corsair, Modelo: Vengeance, Clock: 3200Mhz, Capacidade: 8GB, Tecnologia: DDR4",
        "category": "Memoria RAM",
    },
    {
        "model": "Memória Kingston HyperX Fury RGB 8GB DDR4 3000MHz",
        "img": "https://static.meupc.net/produto/memoria-kingston-hyperx-fury-rgb-8-gb-hx430c15fb3a8-bin64H-L.jpg",
        "price": 471.12,
        "description": "Marca: Kingston, Modelo: HyperX Fury RGB, Clock: 3000Mhz, Capacidade: 8GB, Tecnologia: DDR4",
        "category": "Memoria RAM",
    },
    {
        "model": "Memória Kingston HyperX Fury 8 GB DDR4 2666MHZ",
        "img": "https://static.meupc.net/produto/memoria-kingston-hyperx-fury-hx426c16fb38-u3v75j-L.jpg",
        "price": 289.9,
        "description": "Marca: Kingston, Modelo: HyperX Fury RGB, Clock: 3000Mhz, Capacidade: 8GB, Tecnologia: DDR4",
        "category": "Memoria RAM",
    },
    {
        "model": "Memória G.Skill TridentZ RGB 16 GB (2x8 GB) DDR4-3200",
        "img": "https://static.meupc.net/produto/memoria-gskill-trident-z-16gb-f43200c16d16gtzr-upZ77c-L.jpg",
        "price": 903.93,
        "description": "Marca: G.Skill, Modelo: Tridentz RGB, Clock: 3200Mhz, Capacidade: 2x8GB, Tecnologia: DDR4",
        "category": "Memoria RAM",
    },
    {
        "model": "Memória G.Skill Aegis 16 GB (2x8 GB) DDR4-3200",
        "img": "https://static.meupc.net/produto/memoria-gskill-aegis-f43200c16d16gis-v5Mo5B-L.jpg",
        "price": 770.93,
        "description": "Marca: G.Skill, Modelo: Aegis, Clock: 3200Mhz, Capacidade: 2x8GB, Tecnologia: DDR4",
        "category": "Memoria RAM",
    },
    {
        "model": "HDD Seagate 2TB Barracuda, SATA, 6GB/s",
        "img": "https://static.meupc.net/produto/hdd-seagate-skyhawk-barracuda2tb-wJ8e5F-L.jpg",
        "price": 458.71,
        "description": "Marca: Seagate, Modelo: ST2000DM008, Capacidade: 2TB, RPM: 7200, Cache: 256MB, Tipo: HDD, Saída: SATA",
        "category": "Armazenamento",
    },
    {
        "model": "SSD Sandisk Plus 480GB, SATA, Leitura 535MB/s, Gravação 445MB/s",
        "img": "https://static.meupc.net/produto/ssd-sandisk-ssd-plus-sdssda480gg26-yA3J75-L.jpg",
        "price": 492.82,
        "description": "Marca: Sandisk, Modelo: SDSSDA-480-G26, Capacidade: 480GB, Tipo: SSD, Saída: SATA",
        "category": "Armazenamento",
    },
    {
        "model": "SSD Samsung 970 EVO Plus 1TB, M.2 NVMe, Leitura 3500MB/s, Gravação 3300MB/s",
        "img": "https://static.meupc.net/produto/ssd-samsung-970-evo-plus-970evoplus1tb-ma4uu6-L.jpg",
        "price": 1281.35,
        "description": "Marca: Samsung, Modelo: MZ-V7S1T0B/AM, Capacidade: 1TB, Tipo: SSD, Saída: M.2 NVMe",
        "category": "Armazenamento",
    },
    {
        "model": 'HDD Toshiba P300 3.5" 7200 RPM',
        "img": "https://static.meupc.net/produto/hdd-toshiba-p300-p3001tb-gre9S7-L.jpg",
        "price": 299.99,
        "description": "Marca: Toshiba, Modelo: P300, Capacidade: 1TB, Tipo: HDD, RPM: 7200, Cache: 64 MB, Saída: SATA",
        "category": "Armazenamento",
    },
    {
        "model": "SSD Gigabyte Aorus M.2-2280",
        "img": "https://static.meupc.net/produto/ssd-gigabyte-ud-pro-aorusrgb512gb-jbd7v5-L.jpg",
        "price": 762.9,
        "description": "Marca: Gigabyte, Modelo: Aorus RGB 512GB, Capacidade: 512GB, Tipo: SSD, Saída: M.2 NVMe",
        "category": "Armazenamento",
    },
    {
        "model": "SSD Lexar NM100 M.2-2280 ",
        "img": "https://static.meupc.net/produto/ssd-lexar-aorus-nm100256gb-wer98Q-L.jpg",
        "price": 269.9,
        "description": "Marca: Lexar, Modelo: LNM100-256RBNA, Capacidade: 256GB, Tipo: SSD, Saída: M.2 NVMe",
        "category": "Armazenamento",
    },
    {
        "model": "Gabinete Nox Hummer TGM ATX Mid Tower (Preto)",
        "img": "https://static.meupc.net/produto/gabinete-nox-hummer-tgm-nxhummertgm-zg8ec8-L.jpg",
        "price": 399.9,
        "description": "Marca: Nox Hummer, Modelo: TGM, Tamanho: Mid Tower, Baia Interna 2.5: 2, Baia Interna 3.5: 2, Tamanho máximo da placa de vídeo: 370mm, Dimensões: 420 x 198 x 440 mm",
        "category": "Gabinete",
    },
    {
        "model": "Gabinete Deepcool MATREXX 50 ATX Mid Tower (Preto)",
        "img": "https://static.meupc.net/produto/gabinete-deepcool-matrexx-50-matrexx50-mZZs74-L.jpg",
        "price": 432.8,
        "description": "Marca: Deelcool, Modelo: MATREXX 50, Tamanho: Mid Tower, Baia Interna 2.5: 4, Baia Interna 3.5: 2, Tamanho máximo da placa de vídeo: 340mm, Dimensões: 442 x 210 x 479 mm",
        "category": "Gabinete",
    },
    {
        "model": "Gabinete Sharkoon M25 ATX Mid Tower (Branco)",
        "img": "https://static.meupc.net/produto/gabinete-sharkoon-m25-m25w-z3zGm5-L.jpg",
        "price": 329.25,
        "description": "Marca: Sharkoon, Modelo: M25, Tamanho: Mid Tower, Baia Interna 2.5: 2, Baia Interna 3.5: 2, Tamanho máximo da placa de vídeo: 400mm, Dimensões: 450 x 465 x 210 mm",
        "category": "Gabinete",
    },
    {
        "model": "Gabinete Corsair Carbide 275R ATX Mid Tower (Preto)",
        "img": "https://static.meupc.net/produto/gabinete-corsair-carbide-275r-cc9011130ww-fn28rh-L.jpg",
        "price": 412.3,
        "description": "Marca: Corsair, Modelo: Carbide 275R, Tamanho: Mid Tower, Baia Interna 2.5: 3, Baia Interna 3.5: 2, Tamanho máximo da placa de vídeo: 370mm, Dimensões: 460 x 215 x 455 mm",
        "category": "Gabinete",
    },
    {
        "model": "Gabinete Cooler Master MASTERBOX MB520 ARGB ATX Mid Tower (Preto)",
        "img": "https://static.meupc.net/produto/gabinete-cooler-master-masterbox-mb520-argb-mcbb520kgnnrga-b65n9j-L.jpg",
        "price": 849.9,
        "description": "Marca: Cooler Master, Modelo: MASTERBOX MB520 ARGB, Tamanho: Mid Tower, Baia Interna 2.5: 6, Baia Interna 3.5: 2, Tamanho máximo da placa de vídeo: 400mm, Dimensões: 496 x 217 x 469 mm",
        "category": "Gabinete",
    },
    {
        "model": "Gabinete Corsair iCUE 220T ATX Mid Tower (Preto / Branco)",
        "img": "https://static.meupc.net/produto/gabinete-corsair-icue-220t-cc9011191ww-eQn68C-L.jpg",
        "price": 738.9,
        "description": "Marca: Corsair, Modelo: iCUE 220T, Tamanho: Mid Tower, Baia Interna 2.5: 2, Baia Interna 3.5: 2, Tamanho máximo da placa de vídeo: 300mm, Dimensões: 395 x 210 x 450 mm",
        "category": "Gabinete",
    },
    {
        "model": "Fonte Corsair CV550 550 W ATX",
        "img": "https://static.meupc.net/produto/fonte-corsair-cv-cv550550w80plusbronze-t8T6tP-L.jpg",
        "price": 289.9,
        "description": "Marca: Corsair, Modelo: CV550, Potência: 550 W, Voltagem: 100-240V, Certificado: 80+ Bronze",
        "category": "Fonte",
    },
    {
        "model": "Fonte AeroCool KCAS 400 W ATX",
        "img": "https://static.meupc.net/produto/fonte-aerocool-mwe-white-series-kcas-w9GtN9-L.jpg",
        "price": 229.9,
        "description": "Marca: Corsair, Modelo: KCAS, Potência: 400 W, Voltagem: 100-240V, Certificado: 80+",
        "category": "Fonte",
    },
    {
        "model": "Fonte Corsair CX750M 750 W ATX12V",
        "img": "https://static.meupc.net/produto/fonte-corsair-cxm-cx750m-hNkw98-L.jpg",
        "price": 929.9,
        "description": "Marca: Corsair, Modelo: CX750M, Potência: 750 W, Voltagem: 100-240V, Certificado: 80+ Bronze",
        "category": "Fonte",
    },
    {
        "model": "Fonte Corsair HX1000i 1000 W ATX12V / EPS12V",
        "img": "https://static.meupc.net/produto/fonte-corsair-hxi-hx1000i-cVL24I-L.jpg",
        "price": 4583.42,
        "description": "Marca: Corsair, Modelo: HX1000i, Potência: 1000 W, Voltagem: 100-240V, Certificado: 80+ Platinum",
        "category": "Fonte",
    },
    {
        "model": "Fonte Corsair CX650 650 W ATX12V",
        "img": "https://static.meupc.net/produto/fonte-corsair-cx-cx650-nT564J-L.jpg",
        "price": 409.9,
        "description": "Marca: Corsair, Modelo: CX650, Potência: 650 W, Voltagem: 100-240V, Certificado: 80+ Bronze",
        "category": "Fonte",
    },
    {
        "model": "Fonte Corsair RM650X 650 W ATX12V / EPS12V",
        "img": "https://static.meupc.net/produto/fonte-corsair-rmx-rm650x-utG2k5-L.jpg",
        "price": 719.9,
        "description": "Marca: Corsair, Modelo: RM650X, Potência: 650 W, Voltagem: 100-240V, Certificado: 80+ Gold",
        "category": "Fonte",
    },
    {
        "model": "Teclado Redragon Kumara",
        "img": "https://static.meupc.net/produto/teclado-redragon-kumara-k552-AZ74wy-L.jpg",
        "price": 229.9,
        "description": "Marca: Redragon, Modelo: Kumara, Tipo: Mecânico, Switch: Outemu Blue, Numérico: Não",
        "category": "Perifericos",
    },
    {
        "model": "Teclado HyperX Alloy Origins Core",
        "img": "https://static.meupc.net/produto/teclado-hyperx-alloy-origins-core-hxkb7rdxbr-CKp86Q-L.jpg",
        "price": 529.9,
        "description": "Marca: HyperX, Modelo: Alloy Origins Core, Tipo: Mecânico, Switch: HyperX Red, Numérico: Não",
        "category": "Perifericos",
    },
    {
        "model": "Teclado Razer Huntsman",
        "img": "https://static.meupc.net/produto/teclado-razer-blackwidow-x-chroma-blackwidowxchroma-m4Wdo6-L.jpg",
        "price": 1961.71,
        "description": "Marca: Razer, Modelo: Huntsman, Tipo: Mecânico, Switch: Razer Purple, Numérico: Sim",
        "category": "Perifericos",
    },
    {
        "model": "Teclado Multilaser TC160",
        "img": "https://static.meupc.net/produto/teclado-multilaser-tc160-tx2S76-L.jpg",
        "price": 39.9,
        "description": "Marca: Multilaser, Modelo: TC160, Tipo: Membrana, Switch: Membrana, Numérico: Sim",
        "category": "Perifericos",
    },
    {
        "model": "Monitor LG 29UM69G-B 29.0″ 2560 x 1080 75 Hz",
        "img": "https://static.meupc.net/produto/monitor-lg-29um69g-b-29um69gb-DrGS59-L.jpg",
        "price": 1599.41,
        "description": "Marca: LG, Modelo: 29UM69G-B, Tamanho: 29, Resolução: 2560x1080, Taxa de atualização: 75Hz, Voltagem: 100-240V, Portas: 1x DisplayPort + 1x HDMI",
        "category": "Perifericos",
    },
    {
        "model": "Monitor Acer KG241Q 23.6″ 1920 x 1080 144 Hz",
        "img": "https://static.meupc.net/produto/monitor-acer-kg241q-CyA62g-L.jpg",
        "price": 1429.22,
        "description": "Marca: Acer, Modelo: KG241Q, Tamanho: 23.6, Resolução: 1920x1080, Taxa de atualização: 144Hz, Voltagem: 100-240V, Portas: 1x DisplayPort + 1x HDMI",
        "category": "Perifericos",
    },
    {
        "model": "Monitor AOC 24G2/BK 23.8″ 1920 x 1080 144 Hz",
        "img": "https://static.meupc.net/produto/monitor-aoc-24g2bk-ARs95r-L.jpg",
        "price": 1629.9,
        "description": "Marca: AOC, Modelo: 24G2/BK, Tamanho: 29, Resolução: 1920x1080, Taxa de atualização: 144Hz, Voltagem: 100-240V, Portas: 1x DisplayPort + 2x HDMI + 1x VGA",
        "category": "Perifericos",
    },
    {
        "model": "Monitor LG 34GL750 34.0″ 2560 x 1080 144 Hz",
        "img": "https://static.meupc.net/produto/monitor-lg-ultrawide-34gl750-b6zg7A-L.jpg",
        "price": 2899.9,
        "description": "Marca: LG, Modelo: 34GL750, Tamanho: 34, Resolução: 2560x1080, Taxa de atualização: 144Hz, Voltagem: 100-240V, Portas: 1x DisplayPort + 2x HDMI",
        "category": "Perifericos",
    },
    {
        "model": "Monitor LG 29WK600 29.0″ 2560 x 1080 75 Hz",
        "img": "https://static.meupc.net/produto/monitor-lg-29wk600-B9VD4N-L.jpg",
        "price": 1427.98,
        "description": "Marca: LG, Modelo: 29WK600, Tamanho: 29, Resolução: 2560x1080, Taxa de atualização: 75Hz, Voltagem: 100-240V, Portas: 1x DisplayPort + 2x HDMI",
        "category": "Perifericos",
    },
    {
        "model": "Monitor Asus VG32VQ 31.5″ 2560 x 1440 144 Hz",
        "img": "https://static.meupc.net/produto/monitor-asus-vg32vq-m3Tr56-L.jpg",
        "price": 2799,
        "description": "Marca: Asus, Modelo: VG32VQ, Tamanho: 31.5, Resolução: 2560x1440, Taxa de atualização: 144Hz, Voltagem: 100-240V, Portas: 1x DisplayPort + 2x HDMI",
        "category": "Perifericos",
    },
    {
        "model": "Mouse Logitech G PRO Wireless",
        "img": "https://static.meupc.net/produto/mouse-logitech-g-pro-gpro-u7vki2-L.jpg",
        "price": 632.95,
        "description": "Marca: Logitech, Modelo: G PRO Wireless",
        "category": "Perifericos",
    },
    {
        "model": "Mouse Razer Deathadder V2",
        "img": "https://static.meupc.net/produto/mouse-razer-deathadder-v2-deathadderv2-BFyH82-L.jpg",
        "price": 408.91,
        "description": "Marca: Razer, Modelo: Deathadder",
        "category": "Perifericos",
    },
    {
        "model": "Mouse Logitech G203",
        "img": "https://static.meupc.net/produto/mouse-logitech-g203-mMk88m-L.jpg",
        "price": 112.9,
        "description": "Marca: Logitech, Modelo: G203",
        "category": "Perifericos",
    },
    {
        "model": "Mouse Multilaser MO270",
        "img": "https://static.meupc.net/produto/mouse-multilaser-mo270-zQX9U2-L.jpg",
        "price": 39.89,
        "description": "Marca: Multilaser, Modelo: MO270",
        "category": "Perifericos",
    },
    {
        "model": "Mouse HyperX Pulsefire FPS PRO",
        "img": "https://static.meupc.net/produto/mouse-hyperx-pulsefire-fps-pro-pulsefirefpspro-Aw388X-L.jpg",
        "price": 258.9,
        "description": "Marca: HyperX, Modelo: Pulsefire FPS PRO",
        "category": "Perifericos",
    },
]


def populate_category():
    categories = [
        "Armazenamento",
        "Cooler",
        "Fonte",
        "Gabinete",
        "Perifericos",
        "Memoria Ram",
        "Placa De Video",
        "Placa Mae",
        "Processador",
    ]

    if not CategoryModel.query.all():
        category_to_add = [
            CategoryModel(**{"name": category}) for category in categories
        ]
        db.session.add_all(category_to_add)
        db.session.commit()


def populate_product():
    for product in products:
        product["category"] = product["category"].title()

        category = product.pop("category")

        category_model: CategoryModel = CategoryModel.query.filter_by(
            name=category
        ).first()

        product["category_id"] = category_model.category_id

    if not ProductModel.query.all():
        products_to_add = [ProductModel(**product) for product in products]
        db.session.add_all(products_to_add)
        db.session.commit()


def create_category(category):
    session = db.session

    data = {"name": category}

    category_to_add = CategoryModel(**data)

    session.add(category_to_add)
    session.commit()
