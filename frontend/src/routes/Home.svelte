<!-- svelte는 하나의 페이지에서 표시되는 내용만 변경하는 것 -->
<!-- 하나의 코드로 구현하기 힘들고 복잡해서 따로 만든 후 가져와서 사용한다. -->

<script>
    import fastapi from "../lib/api"
    import { link } from 'svelte-spa-router'

    let jobkorea_list = []
  
    function get_jobkorea_list() {
        fastapi('get', '/api/data/jobkorea', {}, (json) => {
            jobkorea_list = json
        })
    }
  
    get_jobkorea_list()
  </script>
  
