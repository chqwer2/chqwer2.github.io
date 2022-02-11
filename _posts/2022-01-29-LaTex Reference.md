---
layout:     post
title:      "LaTex Fast Reference"
subtitle:   " \"LaTex is Beautiful!\""
date:       2022-01-29 12:00:00
author:     "Calvchen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Tex
    - Starter
    - Writing

---

> “This contains many math symbols I encountered while writing Tex, so I gather them around for fast reference. ”



### Emoji

🌆🌇⭐⚾⚽⚡⚠🆒🚲🚀❔❓❗❕❌

🍣😉😜😱🔥🌊🌈📌💻🎸🎻🎺🎵🎶🍦🌑🌓🌔🌕

[Have Fun with Emoji Unicode](https://apps.timwhitlock.info/emoji/tables/unicode#block-6c-other-additional-symbols)

### Text

| Renders                                         | LaTeX markup          | Renders                   | LaTeX markup     |
| ----------------------------------------------- | --------------------- | ------------------------- | ---------------- |
| $a \quad b \qquad c$                            | `\quad \qquad`        | $a\!b\,c\:d\;e$           | `\ +i,:;_`       |
| $\mathcal{ABC}$                                 | `\mathcal`            | $\mathscr{ABC}$           | `\mathscr`       |
| $\mathbb{ABC}$                                  | `\mathbb`             | $\mathfrak{ABC}$          | `\mathfrak`      |
| $\mathsf{ABC}$                                  | `\mathsf`             | $\mathbf{ABC}$            | `\mathbf`        |
| $\ell\ \Re\ \mho$                               | `\ell \Re \mho`       | $\log \lg \ln$            | `\log \lg \ln`   |
| $\ldots  \cdots$                                | `\ldots cdots`        | $\vdots \ddots$           | `\vdots ddots`   |
| $\bar a\ \vec a\ \hat a$                        | `\bar \vec \hat`      | $\tilde{a} \widetilde{a}$ | `\tilde \wide+X` |
| $$                                              | ``                    | $\acute{a}\  \grave{a}$   | `\acute \grave`  |
| $\check a \  \breve a$                          | `\check \breve`       | $\dot a \ \ddot a$        | `\dot \ddot`     |
| $\overline{a+b}$                                | `\overline`           | $\underline{a+b}$         | `\underline`     |
| $\underset {\theta }{X}\ \overset{\theta }{X} $ | `\underset \overset ` | $$                        | `\overset`       |

Color offered: $\color{grey}{grey}\ \color{purple}{purple}\ \color{maroon}{maroon}\ \color{olive}{olive}\ \color{silver}{silver}\ \color{navy}{navy}\ \color{lime}{lime} \color{teal}{teal}$

Markup `\overbrace{a + \underbrace{b+c}_{1.0} + d}^{2.0}` will render below:


$$
\overbrace{a+\underbrace{b+c}_{1.0}+d}^{2.0}
$$


The enclose package haven’t provided…

| $$\enclose{horizontalstrike}{a}\ \enclose{verticalstrike}{a}$$ | `\enclose{horizontalstrike}` | $\enclose{updiagonalstrike}{a} \enclose{downdiagonalstrike}{a}$ | `up/down + diagonalstrike` |
| ------------------------------------------------------------ | ---------------------------- | ------------------------------------------------------------ | -------------------------- |
| $\enclose{updiagonalstrike,downdiagonalstrike}{a}$           | `up,downdiagonalstrike`      |                                                              |                            |

### Greek Letters

| Renders                                                      | LaTeX markup              | Renders                                                      | LaTeX markup        |
| ------------------------------------------------------------ | ------------------------- | ------------------------------------------------------------ | ------------------- |
| ![{\displaystyle \alpha A}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1423e0a85ebc0eacd23bce6800aac8f222548cb1) | `\alpha A`                | ![{\displaystyle \nu N}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ae155e152964cc8ca332708abdd014d9362b1959) | `\nu N`             |
| ![{\displaystyle \beta B}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e86ade6391d9979a1ec9ef888a69c8e1bfaca861) | `\beta B`                 | ![{\displaystyle \xi \Xi }](https://wikimedia.org/api/rest_v1/media/math/render/svg/58db043ab673381e890f325efefdf7eee06d9acd) | `\xi \Xi`           |
| ![{\displaystyle \gamma \Gamma }](https://wikimedia.org/api/rest_v1/media/math/render/svg/0a703b97315b40b657673479ae39d6e6f8fecbe1) | `\gamma \Gamma`           | ![{\displaystyle oO\;}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6c5cb490780176f943464dc5313ec8eb2a6285d4) | `o O`               |
| ![{\displaystyle \delta \Delta }](https://wikimedia.org/api/rest_v1/media/math/render/svg/7ec33521315a7ca8e815f20024d2b9494b8123b3) | `\delta \Delta`           | ![{\displaystyle \pi \Pi }](https://wikimedia.org/api/rest_v1/media/math/render/svg/ab5a189a040911908efdcededa3d4e40e48ae602) | `\pi \Pi`           |
| ![{\displaystyle \epsilon \varepsilon E\;}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ace20d40a97f4bcd3d5a0efbdee5513c241fe016) | `\epsilon \varepsilon E`  | ![{\displaystyle \rho \varrho P\;}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a4cf38723a1cd25888c0c3c828e09f01ab04b012) | `\rho \varrho P`    |
| ![{\displaystyle \zeta Z}](https://wikimedia.org/api/rest_v1/media/math/render/svg/98de1aceefc11746f0bd397a8c7954cad5a0a6ce) | `\zeta Z`                 | ![{\displaystyle \sigma \,\!\Sigma \;}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9689e4eb34d33e1d734a3044d9d35a89680f0dc3) | `\sigma \Sigma`     |
| ![{\displaystyle \eta H}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0aa854c7fa2f3b73dfc306fd9d2c3d79105e80e3) | `\eta H`                  | ![{\displaystyle \tau T}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d9c0bbf08b46b2399edbd6f01cdc029da3abfa7f) | `\tau T`            |
| ![{\displaystyle \theta \vartheta \Theta }](https://wikimedia.org/api/rest_v1/media/math/render/svg/083985203afdb520647be7a9b79acda20074e744) | `\theta \vartheta \Theta` | ![{\displaystyle \upsilon \Upsilon }](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d75a091b694acee6aeb07edc29b0f507a76ee59) | `\upsilon \Upsilon` |
| ![{\displaystyle \iota I}](https://wikimedia.org/api/rest_v1/media/math/render/svg/698f27066de7dd25ab2a00dac02995172fbbbcfa) | `\iota I`                 | ![{\displaystyle \phi \varphi \Phi }](https://wikimedia.org/api/rest_v1/media/math/render/svg/3a540725a8834facfdc76786932db303403f8347) | `\phi \varphi \Phi` |
| ![{\displaystyle \kappa K}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8714fc0053e3bc115a8ab0e2e5044529a79541e8) | `\kappa K`                | ![{\displaystyle \chi X}](https://wikimedia.org/api/rest_v1/media/math/render/svg/49a711f6b26e350769bea7258cf6b50cf22f5c91) | `\chi X`            |
| ![{\displaystyle \lambda \Lambda \;}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cbf5521f6c5782d76a904953cc3ad1928ea8e615) | `\lambda \Lambda`         | ![{\displaystyle \psi \Psi }](https://wikimedia.org/api/rest_v1/media/math/render/svg/eeab56671924f9300f94dd188d0ab8d40d0d3d63) | `\psi \Psi`         |
| ![{\displaystyle \mu M}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7cb72c559885487b695afaea0096ad43ac3323a1) | `\mu M`                   | ![{\displaystyle \omega \Omega }](https://wikimedia.org/api/rest_v1/media/math/render/svg/712b9bf23b1404718331d8f2a4deab1a7c3ca46c) | `\omega \Omega `    |

### Mathematical modes

| Renders       | LaTeX markup | Renders               | LaTeX markup |
| ------------- | ------------ | --------------------- | ------------ |
| $\sum$        | `\sum`       | $\prod$               | `\prob`      |
| $\sqrt[y]{X}$ | `\sqrt[y]`   | $\lim_{n \to \infty}$ | `\lim`       |
| $\int$        | `\int`       | $\oint$               | `\oint`      |
| $\sqrt{X}$    | `\sqrt`      | $\iiint$              | `\iiint`     |
| $\propto $    | `\propto `   | $\approx$             | `\approx`    |
| $\pmod{m}$    | `\pmod`      | $a \bmod b$           | `\bmod`      |

### Arrows

| Renders                                                      | LaTeX markup           | Renders                                                      | LaTeX markup         |
| ------------------------------------------------------------ | ---------------------- | ------------------------------------------------------------ | -------------------- |
| $\leftarrow \Leftarrow$                                      | `\l/Leftarrow`         | $$                                                           | `\Leftarrow`         |
| $\rightarrow\ \Longrightarrow$                               | `\rightarrow Long+X `  | $\rightleftharpoons$                                         | `\rightleftharpoons` |
| $\uparrow \ \Uparrow$                                        | `\u/Uparrow`           | $\downarrow \ \Downarrow$                                    | `\d/Downarrow`       |
| $\leftrightarrow\ \Leftrightarrow\ \Updownarrow$             | `\Leftright/Updown+X ` |                                                              | `\`                  |
| ![{\displaystyle \mapsto }](https://wikimedia.org/api/rest_v1/media/math/render/svg/bc09de045e7d82eef9fe078e7e7606576640c11b) | `\mapsto Long+X`       |                                                              |                      |
| ![{\displaystyle \nearrow }](https://wikimedia.org/api/rest_v1/media/math/render/svg/13726ca48b64be8035bbf69dedc5de51b6c59b62) | `\nearrow`             | ![{\displaystyle \searrow }](https://wikimedia.org/api/rest_v1/media/math/render/svg/c086f3b8ec7a49977877c105da5f386531d5775a) | `\searrow`           |
| ![{\displaystyle \swarrow }](https://wikimedia.org/api/rest_v1/media/math/render/svg/b4fafa2f8a9f4c7b1c1adcf090888097ddde887d) | `\swarrow `            | ![{\displaystyle \nwarrow }](https://wikimedia.org/api/rest_v1/media/math/render/svg/8477be47a1b75007f7f62bb406e08f5405366f2a) | `\nwarrow`           |
| ![{\displaystyle \leftharpoonup }](https://wikimedia.org/api/rest_v1/media/math/render/svg/ed5b4c2f2ab115005b72687fbe5e6584497a0b17) | `\leftharpoonup  `     | ![{\displaystyle \rightharpoonup }](https://wikimedia.org/api/rest_v1/media/math/render/svg/912c85b375886509f9bf323bab01cd1d3d0b96c1) | `\rightharpoonup`    |
| ![{\displaystyle \leftharpoondown }](https://wikimedia.org/api/rest_v1/media/math/render/svg/8572e40b7a21ea071eac94f81458238d9f096ff8) | `\leftharpoondown `    | ![{\displaystyle \rightharpoondown }](https://wikimedia.org/api/rest_v1/media/math/render/svg/b3b850cb314e0167a03944481381f8a0401506d8) | `\rightharpoondown`  |

### Miscellaneous symbols

| Renders                                                      | LaTeX markup   | Renders                                                      | LaTeX markup  |
| ------------------------------------------------------------ | -------------- | ------------------------------------------------------------ | ------------- |
| ![{\displaystyle \infty \;\;}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7e636ab1710fb09518c89fb6777597377fe79f0f) | `\infty`       | ![{\displaystyle \forall \;}](https://wikimedia.org/api/rest_v1/media/math/render/svg/025c7b257d7948331271a151fe460cdce3c69167) | `\forall`     |
| ![{\displaystyle \Re }](https://wikimedia.org/api/rest_v1/media/math/render/svg/2cc5a2cb7aa22f6d765976edb1daebefaf408142) | `\Re`          | ![{\displaystyle \Im }](https://wikimedia.org/api/rest_v1/media/math/render/svg/d3e0312a4871a615cbdae168be102907f0a51e95) | `\Im`         |
| ![{\displaystyle \nabla }](https://wikimedia.org/api/rest_v1/media/math/render/svg/a3d0e93b78c50237f9ea83d027e4ebbdaef354b2) | `\nabla`       | ![{\displaystyle \exists }](https://wikimedia.org/api/rest_v1/media/math/render/svg/77ed842b6b90b2fdd825320cf8e5265fa937b583) | `\exists`     |
| ![{\displaystyle \partial }](https://wikimedia.org/api/rest_v1/media/math/render/svg/62b4e7c1cedb9564609aefd2aa2309972f455c24) | `\partial`     | ![{\displaystyle \nexists }](https://wikimedia.org/api/rest_v1/media/math/render/svg/105571be31b330ddf22ac965fc50efedfb59de7d) | `\nexists`    |
| ![{\displaystyle \emptyset }](https://wikimedia.org/api/rest_v1/media/math/render/svg/6af50205f42bb2ec3c666b7b847d2c7f96e464c7) | `\emptyset`    | ![{\displaystyle \varnothing \;}](https://wikimedia.org/api/rest_v1/media/math/render/svg/73f3c132d4a55444673503c4498310ea7cdd7df5) | `\varnothing` |
| ![{\displaystyle \wp }](https://wikimedia.org/api/rest_v1/media/math/render/svg/f4050ebf63686af152bf1ef5caabcdf2a2d812cf) | `\wp`          | ![{\displaystyle \complement }](https://wikimedia.org/api/rest_v1/media/math/render/svg/6b2479e2cdb7ce0c5be60408f111d2354369189f) | `\complement` |
| ![{\displaystyle \neg }](https://wikimedia.org/api/rest_v1/media/math/render/svg/fa78fd02085d39aa58c9e47a6d4033ce41e02fad) | `\neg`         | ![{\displaystyle \cdots }](https://wikimedia.org/api/rest_v1/media/math/render/svg/e1d67495288eac0fa90d5bbcad7d9a343c15ad56) | `\cdots`      |
| ![{\displaystyle \square }](https://wikimedia.org/api/rest_v1/media/math/render/svg/455831d58fa08f311b934d324adcff89a868b4e4) | `\square`      | ![{\displaystyle \surd }](https://wikimedia.org/api/rest_v1/media/math/render/svg/8a9d637675e4ee00572431a0e42fa556901a4ca8) | `\surd `      |
| ![{\displaystyle \blacksquare }](https://wikimedia.org/api/rest_v1/media/math/render/svg/8733090f2d787d03101c3e16dc3f6404f0e7dd4c) | `\blacksquare` | ![{\displaystyle \triangle }](https://wikimedia.org/api/rest_v1/media/math/render/svg/d909fe94e8277a4c44a50853cb7dbbf0fa3148ed) | `\triangle`   |

### Binary Operation/Relation Symbols

| Renders                                                      | LaTeX markup | Renders                                                      | LaTeX markup      |
| ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ | ----------------- |
| $\pm$                                                        | `\pm`        | $\not >$                                                     | `\not`            |
| ![{\displaystyle \times }](https://wikimedia.org/api/rest_v1/media/math/render/svg/0ffafff1ad26cbe49045f19a67ce532116a32703) | `\times`     | $\cdot \circ \ast$                                           | `cdot circ ast`   |
| ![{\displaystyle \div }](https://wikimedia.org/api/rest_v1/media/math/render/svg/837b35ee5d25b5ce7b07f292c27cc90533dd9fd4) | `\div`       | ![{\displaystyle \cap }](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d4e886e6f5a28a33e073fb108440c152ecfe2d3) | `\cap`            |
| $\cup\  \cap$                                                | `\cup \cap`  | ![{\displaystyle \neq \;}](https://wikimedia.org/api/rest_v1/media/math/render/svg/fdd9cfbf0e9468f24b6f9b27db3be1f8bb5d6650) | `\neq`            |
| $\leq\ \geq$                                                 | `leq geq`    | $\ll\ \gg$                                                   | `ll gg `          |
| ![{\displaystyle \in }](https://wikimedia.org/api/rest_v1/media/math/render/svg/6fe4d5b0a594c1da89b5e78e7dfbeed90bdcc32f) | `\in`        | ![{\displaystyle \perp \;}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e359e464318097f841e700d97bdb60c5aed21cf5) | `\perp`           |
| ![{\displaystyle \notin }](https://wikimedia.org/api/rest_v1/media/math/render/svg/33dea9a3a3f311cc734ffd570e8f697ea1560a90) | `\notin`     | $\subset$ $\supset$                                          | `\subset \supset` |
| ![{\displaystyle \simeq }](https://wikimedia.org/api/rest_v1/media/math/render/svg/65b9738551241417d16d9843525ed52410af4dc9) | `\simeq`     | ![{\displaystyle \approx }](https://wikimedia.org/api/rest_v1/media/math/render/svg/6f58f4c2b73283ce8a5ad28fb3746f2a8c998789) | `\approx`         |
| ![{\displaystyle \wedge }](https://wikimedia.org/api/rest_v1/media/math/render/svg/1caa4004cb216ef2930bb12fe805a76870caed94) | `\wedge`     | ![{\displaystyle \vee }](https://wikimedia.org/api/rest_v1/media/math/render/svg/7b76220c6805c9b465d6efbc7686c624f49f3023) | `\vee`            |
| ![{\displaystyle \oplus \;}](https://wikimedia.org/api/rest_v1/media/math/render/svg/282868a7bc101b11dabe70abe1d72def8ec688c3) | `\oplus`     | ![{\displaystyle \otimes }](https://wikimedia.org/api/rest_v1/media/math/render/svg/de29098f5a34ee296a505681a0d5e875070f2aea) | `\otimes`         |
| $\bigodot$                                                   | `\bigodot`   | $\ominus$                                                    | `\bigominus`      |
| ![{\displaystyle \Box }](https://wikimedia.org/api/rest_v1/media/math/render/svg/029b77f09ebeaf7528fc831fe57848be51f2240b) | `\Box`       | ![{\displaystyle \boxtimes }](https://wikimedia.org/api/rest_v1/media/math/render/svg/0cfc27ef694886c0b78697df1cd69558cdf53eff) | `\boxtimes`       |
| ![{\displaystyle \equiv }](https://wikimedia.org/api/rest_v1/media/math/render/svg/4c5c34250859b6f6d2a77b4e8a2ceaa90638076d) | `\equiv`     | ![{\displaystyle \cong }](https://wikimedia.org/api/rest_v1/media/math/render/svg/a725ebc5ab8de11d7b71a8aa5a3706c2ea467885) | `\cong`           |
| $\sim$                                                       | `\sim`       | $\tilde{x}$                                                  | `\tilde`          |
| $\because$                                                   | `\because`   | $\therefore$                                                 | `\therefore`      |
| $\exists$                                                    | `\exists`    |                                                              |                   |

### Brackets and Parentheses

| Type                        | LaTeX markup          | Renders as  |
| --------------------------- | --------------------- | ----------- |
| Parentheses; round brackets | `(x+y)`               | (*x*+*y*)   |
| Brackets; square brackets   | `[x+y]`               | [*x*+*y*]   |
| Braces; curly brackets      | `\{ x+y \}`           | {*x*+*y*}   |
| Angle brackets              | `\langle x+y \rangle` | ⟨*x*+*y*⟩   |
| Pipes; vertical bars        | `|x+y|`               | \|*x*+*y*\| |
| Double pipes                | `\|x+y\|`             | ∥*x*+*y*∥   |

- \left[ … \right]  
-  \left( … \right( 
- \Bigg \langle … \bigg \rangle

$$
\left[  \frac{ N } { \left( \frac{L}{p} \right)  - (m+n) }  \right]\\
\left(  \frac{ N } { \left( \frac{L}{p} \right)  - (m+n) }  \right)\\
 \Bigg \langle 3x+7 \bigg \rangle
$$

![image-20220129110413636](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220129110413636.png)

![image-20220129110431210](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20220129110431210.png)



