<!-- 각각의 svelte파일을 가져와 필요한 정보를 표시 -->

<script>
    import Router from 'svelte-spa-router'
    import Home from "./routes/Home.svelte"
    import Detail from "./routes/Detail.svelte"
  
    const routes = {
      '/': Home,
      '/detail/:jk_data_id': Detail,
    }
  </script>
  
  <Router {routes}/>
  