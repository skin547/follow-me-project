(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{28:function(e,t,n){e.exports=n(37)},37:function(e,t,n){"use strict";n.r(t);var a=n(5),c=n(0),r=n.n(c),o=n(22),l=n.n(o),u=n(39),m=n(13),i=n(38),d=n(24),s=n(41),E=function(e){var t=e.content;return r.a.createElement(d.a,null,r.a.createElement(m.b,{to:t},r.a.createElement(s.a,{variant:"outline",size:"lg",block:!0},t)))},f=function(){return r.a.createElement(i.a,{style:{marginTop:"5%",marginBottom:"3%"}},r.a.createElement(E,{content:"About"}),r.a.createElement(E,{content:"LogIn"}),r.a.createElement(E,{content:"TodoList"}))},O=function(){return r.a.createElement(d.a,null,r.a.createElement("h1",null,"WELCOME"))},p=n(12),b=n(42),j=n(40),h=function(e){var t=e.editTodo,n=e.todo,o=Object(c.useState)(n.text),l=Object(a.a)(o,2),u=l[0],m=l[1],i=Object(c.useState)(!0),E=Object(a.a)(i,2),f=E[0],O=E[1],p=Object(c.useState)("Edit"),h=Object(a.a)(p,2),T=h[0],v=h[1];return r.a.createElement(d.a,null,r.a.createElement(b.a,{style:{width:"17rem",marginTop:"2%",marginBottom:"8%"}},r.a.createElement(b.a.Body,null,r.a.createElement(b.a.Title,null,r.a.createElement("input",{type:"checkbox",value:n.completed}),"ID:",n.id,r.a.createElement("hr",null),r.a.createElement(j.a.Control,{as:"textarea",onChange:function(e){m(e.target.value)},plaintext:f,readOnly:f,value:u})),r.a.createElement(s.a,{variant:"info",onClick:function(){O(!f),v(f?"Done":"Edit"),t(n.id,u)}},T))))},T=function(e){var t=e.product,n=Object(c.useState)(t.id),o=Object(a.a)(n,2),l=o[0],u=(o[1],Object(c.useState)(t.title)),m=Object(a.a)(u,2),i=m[0],s=(m[1],Object(c.useState)(t.desc)),E=Object(a.a)(s,2),f=(E[0],E[1],Object(c.useState)(t.price)),O=Object(a.a)(f,2),p=(O[0],O[1],Object(c.useState)(!0)),j=Object(a.a)(p,2),h=(j[0],j[1],Object(c.useState)("Edit")),T=Object(a.a)(h,2);T[0],T[1];return r.a.createElement(d.a,null,r.a.createElement(b.a,{style:{width:"17rem",marginTop:"2%",marginBottom:"8%"}},r.a.createElement(b.a.Body,null,r.a.createElement(b.a.Title,null,"ID:",l,r.a.createElement("hr",null),"Title:",i))))},v=function(e){e.test;var t=Object(c.useState)([]),n=Object(a.a)(t,2),o=n[0],l=n[1];return Object(c.useEffect)(function(){fetch("https://jsonplaceholder.typicode.com/todos/").then(function(e){return e.json()}).then(function(e){return l(e)})},[]),r.a.createElement(i.a,null,o.map(function(e){return r.a.createElement(T,{product:e})}))},g=function(){var e=Object(c.useState)([]),t=Object(a.a)(e,2),n=t[0],o=t[1];return Object(c.useEffect)(function(){fetch("https://jsonplaceholder.typicode.com/users/").then(function(e){return e.json()}).then(function(e){return o(e)})},[]),r.a.createElement("div",null,r.a.createElement("ul",null,n.map(function(e){return r.a.createElement("li",{key:e.username},e.username,": ",e.name)})))},x=function(){return r.a.createElement(d.a,null,r.a.createElement(g,null),r.a.createElement(v,null))},y=function(e){var t=e.todos,n=Object(c.useContext)(I).dispatch,a=function(e,t){n({type:"EDIT_TODO",target:e,text:t})};return r.a.createElement(i.a,null,t.map(function(e){return r.a.createElement(h,{key:e.id,todo:e,editTodo:a})}))},D=function(e){var t=e.addTodo,n=e.resetTodo,o=Object(c.useState)(""),l=Object(a.a)(o,2),u=l[0],m=l[1];return r.a.createElement(j.a,null,r.a.createElement(i.a,null,r.a.createElement(d.a,{xs:"5",sm:"8",ms:"8",lg:"8",xl:"8"},r.a.createElement(j.a.Control,{onChange:function(e){return m(e.target.value)},value:u})),r.a.createElement(d.a,null,r.a.createElement(s.a,{type:"submit",block:!0,onClick:function(e){e.preventDefault(),t(u),m("")}},"Add")),r.a.createElement(d.a,null,r.a.createElement(s.a,{variant:"danger",block:!0,onClick:function(){n()}},"Reset"))))},S=function(){var e=Object(c.useContext)(I),t=e.state,n=e.dispatch;return r.a.createElement(d.a,null,r.a.createElement(D,{resetTodo:function(){n({type:"RESET"})},addTodo:function(e){n({type:"ADD_TODO",text:e,completed:!0})}}),r.a.createElement("hr",null),r.a.createElement(y,{todos:t.todos}))},C=function(){return r.a.createElement(i.a,null,r.a.createElement(d.a,null,r.a.createElement(p.a,{exact:!0,path:"/",component:O}),r.a.createElement(p.a,{exact:!0,path:"/Home",component:O}),r.a.createElement(p.a,{path:"/About",component:x}),r.a.createElement(p.a,{path:"/TodoList",component:S})))},k=n(14),w={todos:[]};function B(e,t){switch(t.type){case"ADD_TODO":var n={id:e.todos.length+1,text:t.text,completed:!1};return{todos:[].concat(Object(k.a)(e.todos),[n])};case"EDIT_TODO":return e.todos.find(function(e){return e.id===t.target}).text=t.text,{todos:Object(k.a)(e.todos)};case"COMPLETE_TODO":return e.todos.forEach(function(e){e.id===t.target&&(e.completed=t.complete)}),{todos:Object(k.a)(e.todos)};case"RESET":return{todos:[]};default:return e}}n.d(t,"TodoContext",function(){return I});var I=Object(c.createContext)({});l.a.render(r.a.createElement(function(){var e=Object(c.useReducer)(B,w),t=Object(a.a)(e,2),n=t[0],o=t[1];return r.a.createElement(I.Provider,{value:{state:n,dispatch:o}},r.a.createElement(m.a,null,r.a.createElement(u.a,{fluid:!0},r.a.createElement(f,null),r.a.createElement(C,null))))},null),document.getElementById("root"))}},[[28,1,2]]]);
//# sourceMappingURL=main.fe2c82ba.chunk.js.map