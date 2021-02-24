const deleteConfirm = (id) =>{
    var ask = confirm('Are you sure to delete employee');
    if (ask && id) {
        window.location.href = "/delete/"+id;
    } else {
    }
    return false;
}
