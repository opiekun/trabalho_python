$( document ).ready(function() {  
    $.ajax({
        url: 'http://localhost:8080/livros',
        method: 'GET',
        dataType: 'json', 
        success:livros_biblioteca, 
        error: function() {
            alert("erro conexao");
        }
    });
    function livros_biblioteca(livro) {
        linhas = ""
        for (var i in livros) {
            linhas += newShelf(livros[i]);
        }
        $("#corpoTabela").html(linhas);
    }  

    function newShelf(livro) {
        return "<tr>" + 
            "<td>" + livro.autor + "</td>" + 
            "<td>" + livro.livro + "</td>" + 
            "<td>" + livro.sessao + "</td>" +
            "</tr>";
    }
  });