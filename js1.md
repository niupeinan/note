Javascript
node.js vue.js

shift+tab+delect:������ǰҳ��(typora)

## ��ɣ�

1.ECMAscript
 ���� �������� ����� ���� ���� ����

2.BOM���������ģ��
 window���� history���� location����

3.DOM�ĵ�����ģ��
 Ԫ�ػ�ȡ �������� ������ʽ �ڵ� �¼� �¼�����



## ���ã�

1.������֤

2.��̬������ɾ��Ԫ��

3.����Ԫ�����ݺ���ʽ

4.ģ�⶯��

5.����cookie

6.ajax

7.JSON��ʽ�����ݴ���
....

## ������

�ͻ��˽ű����ԣ�ʵ���û�������

����'����'��'�¼�����'��'��ɢ��''������'���ԡ�

@import url('base.css'); ����base��

## �ƶ��˲��ֲ��裺

> �Ӿ��ӿ� �����ӿ� �����ӿ�
>
> rem����ʵ������  rem.js      remԭ��root  em  html����ı��� 
>
> em:��ǰ����ı���   html{font-size:;} //��Ƹ��ҳ��ı���   

1. �޸��ӿ�

   ```html
   <meta name="viewport" content="width=device-width">
   ```

2. ����rem.js

   ```html
   <script src=""></script>script>
   ```

3. �޸�rem.js��Ƹ��еĿ��

����ͼƬ

```html
background:url() no-repeat bottom/contain,
//���뱳��ͼƬ ��ֹ�ظ� λ�ã�top bottom left right��
background-size��100% 100%��
//����ͼƬ�Ĵ�С
background-size��contain;
//���տ���еĽϴ�ֵ��������
background-size��cover;
//���տ���еĽ�Сֵ��������
```

## ����

```css
background:linear-gradient(top,��ɫ1����ɫ2��.....)
��һ�����������俪ʼ�ķ���top.left.bottom.right.25deg
��ɫ��red.#fff.rgb(0,0,0).rgba(0,0,0,0)
```

## ������ں�

- -webkit- �ȸ��ں�
- -moz- ���
- -ms- ie
- -o- ŷ��

## ���Բ���

```html
display:flex;
//ָ��Ϊ���Բ���
justify-content:center;
//��Ԫ����ˮƽ����Ķ��뷽ʽ ���ж���
align-items:center;
//��Ԫ���ڴ�ֱ����Ķ��뷽ʽ ���ж���
```

   flex-shrink��0;��ʹ�ռ䲻�㣬��Ԫ�ز���С��

   overflow-x:auto:����������x����ı�����ʽ��

   auto���Զ�����������Զ��Թ���������ʽ��ʾ��

  .recent-hours::-websit-scrolibar{height:0}ȥ��������  eg:.future ul::-webkit-scrollbar{
	height: 0;



## ��ɣ�

 box-sizing ;

### ���⣺

- ȥ�������Ĭ����ʽ

  ```html
  *{
  margin:0;
  padding:0;
  }
  ```

- ҳ���к��ӵ���ʵ��ߡ�

- margic-top��BUG��

  - �ø�Ԫ�ص�padding-topģ����Ԫ�ص�margin-top
  - ����Ԫ�����overflow��hiddon��

- ���ڱ�ǩֻ���������ң������������¼�ࡣ

## flex���֣�

### ���������ԣ�

- flex-direction���������᷽��
  - row��Ĭ��ֵ��������Ϊˮƽ�����������ˡ�
  - `row-reverse`������Ϊˮƽ����������Ҷˡ�
  - `column`������Ϊ��ֱ������������ء�
  - `column-reverse`������Ϊ��ֱ������������ء�

- flex-wrap��������Ŀ����

  - wrap ��Ŀ����
  - nowrap ��Ŀ������

- `flex-flow`������`flex-direction`���Ժ�`flex-wrap`���Եļ�д��ʽ��Ĭ��ֵΪ`row nowrap`��

- `justify-content`���Զ�������Ŀ�������ϵĶ��뷽ʽ��

  - flex-start`��Ĭ��ֵ��������룬��������`
  - flex-end`���Ҷ��룬������յ�`
  - `center`�� ���У����������
  - space-between`�����˶��룬��Ŀ֮��ļ������ȡ�`
  - space-around`��ÿ����Ŀ����ļ����ȡ����ԣ���Ŀ֮��ļ������Ŀ��߿�ļ����һ����

- `align-items`���Զ�����Ŀ�ڽ���������ζ��롣 

  - flex-start`��������������롣
  - flex-end`����������յ���롣`
  - center����������е���롣
  - baseline`: ��Ŀ�ĵ�һ�����ֵĻ��߶��롣`
  - `stretch`��Ĭ��ֵ���������Ŀδ���ø߶Ȼ���Ϊauto����ռ�����������ĸ߶ȡ�

- `align-content`���Զ����˶�����ߵĶ��뷽ʽ�������Ŀֻ��һ�����ߣ������Բ������á� 

  - `flex-start`���뽻����������롣
  - `flex-end`���뽻������յ���롣
  - `center`���뽻������е���롣
  - `space-between`���뽻�������˶��룬����֮��ļ��ƽ���ֲ���
  - `space-around`��ÿ����������ļ������ȡ����ԣ�����֮��ļ����������߿�ļ����һ����
  - `stretch`��Ĭ��ֵ��������ռ�����������ᡣ

## ��Ŀ���ԣ�

- order���Զ�����Ŀ������˳����ֵԽС������Խ��ǰ��Ĭ��Ϊ0�� 
- flex-grow`���Զ�����Ŀ�ķŴ������Ĭ��Ϊ`0`�����������ʣ��ռ䣬Ҳ���Ŵ� `
- `flex-shrink`���Զ�������Ŀ����С������Ĭ��Ϊ1��������ռ䲻�㣬����Ŀ����С�� 
- `flex-basis`���Զ������ڷ������ռ�֮ǰ����Ŀռ�ݵ�����ռ䣨main size�������������������ԣ����������Ƿ��ж���ռ䡣����Ĭ��ֵΪ`auto`������Ŀ�ı�����С��
- flex`������`flex-grow`,?`flex-shrink`?��?`flex-basis`�ļ�д��Ĭ��ֵΪ`0 1 auto`�����������Կ�ѡ��`
- align-self`������������Ŀ����������Ŀ��һ���Ķ��뷽ʽ���ɸ���`align-items`���ԡ�Ĭ��ֵΪ`auto`����ʾ�̳и�Ԫ�ص�`align-items`���ԣ����û�и�Ԫ�أ����ͬ��`stretch`��
  - flex-start ���������
  - flex-end�������յ�
  - center����

## target������������ҳ���д򿪵�λ��

- ?    _self���ڱ����ڴ򿪣�Ĭ��ֵ��

- _blank�����´��ڴ�
- title:����

## �ı�ģ�ͣ�

- ### �ı����У�

  ```css
  word-break:break-all;   //ʹ�����պ��ı�����
  ```

- ###  �����ı����:

  ```css
  // ���ƻ���
  white-space:nowrap;
  overflow:hidden;
  // ����������ʡ�Ժ���ʾ
  text-overflow:ellipsis;
  ```

- ### �����ı������

  ```css
  // ������ָ��Ϊ���Ժ���
  display:-websit-box;
  // �ڵ��Ժ�ģ����ָ��Ԫ�ص��Ų�˳��
  -websit-box-orient:vertical;
  // ָ���ı����������
  -websit-line-clamp:3;
  heightҪ��line-height�ı���
  line-height:70px;
  overflow:hidden;
  ```

## ���ؼ���

- action:����Ϣ�ύ��λ�� <form></form>

- method���ύ�ķ�ʽ

  - ?	get:��ַ������Ϣ�٣���ȫ�Ե�
  - post:��Ϣ���࣬�Ƚϰ�ȫ

- ����� input

  ```css
  �û�����<input type=" text" placeholder="�������û���..." maxlength="10" value="" class="text" name="username" >
  placeholder:Ĭ����ʾ�ı�
  maxlength:�涨���������ַ���
  name���ͺ�̨�������ݽ���
  script:��ȡ��Ϣ
  ��ȡ���㣺.text:focus{
    outline:none  //�������ʧ
  }
  ```

- �����password ���ڿ��ǩ

  ```css
  <br>
  ��&nbsp;��<input type="password" placeholder="����������" name=��psw��>
  <br>
  //��ѡ��ť name���Ե�ֵҪ���
  ��ѡ������Ա�
  <label for="man">
  �У�<input type="radio" name="sex" id="man" checked//Ĭ��ѡ��>
  </label>
  <label for="woman">
  Ů��<input type="radio" name="sex" id="woman">
  </label>
  // ��ѡ��ť
  ��ѡ����ϲ�������֣�
  ҡ��<input type="checkbox" checked>
  // ������
  ��ѡ�����ѧ����
  <select name="" id="">
  	<option value="">˶ʿ</option>
  </select>
  // �ļ�
  ���ϴ���Ƭ��<input type="file">;
  // ���԰壨���ı���
  <textarea name="" id="" cole="" rows=""></textarea>
  textarea{
    resize:none/both/vertical/horizontal;//�Ƿ������û��������ô�С��������/������/ֻ�ܴ�ֱ����/ֻ��ˮƽ����
  }
  //���ð�ť
  <input type="reset">
  //�ύ��ť
  <input type="submit">
  //�Զ��尴ť
  <input type="button" value="��ť">
  <button>����</button>
  //��ɫ
  <input type="color">
  //ʱ������
  ����<input type="month">
  ����<input type="week">
  ʱ��<input type="time">
  ������<input type="data">
  ������ʱ��<input type="datatime-local">
  //��Ƶ��Ƶ
  <audio src="1.mp4" controls loop><audio>
  <video src="1.mp4" controls loop><video>
  controls:�ؼ����û���ʾ
  loop:ѭ������
  autoplay:��ҳ�������ɺ��Զ�����
  //��֤
  <input type="email">
  <input type="tel" autofocus>
   autofocus:�Զ���ȡ����
  ```

##  h5���廯��ǩ ���ǩ

- <header>ͷ��</header>

- <nav>����</nav>
- <aside>�ർ��</saide>
- <section>ҳ���е�ĳһ����</section>
- <footer>�ײ�</footer>
- <main>����</main>


