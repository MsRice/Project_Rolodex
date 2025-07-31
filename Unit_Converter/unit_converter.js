
const temp = [
    {
        'name' : 'Celsius (°C)',
        'unit' : 32
     } , {
        'name' : 'Fahrenheit (°F)',
        'unit' : 32
    
    },{
        'name' : 'Kelvin (K)',
        'unit' : 32
    } , {
        'name' : 'Newton (°N)',
        'unit' : 32
    }]

const length = [
    {
        'name' : 'Inch' ,
        'unit' : 1

    },{
        'name' : 'Centimeter' ,
        'unit' : 2.54

    } ,{
        'name' : 'Foot' ,
        'unit' : 12

    },{
        'name' : 'Mile' ,
        'unit' : 1.5783e-5

    } ,{
        'name' : 'Millimeter' ,
        'unit' : 25.4

    } ,{
        'name' : 'Meter' ,
        'unit' : 0.0254

    } ,{
        'name' : 'Kilometer' ,
        'unit' : 2.54e-5

    } ,{
        'name' : 'Yard' ,
        'unit' : 0.0277778

    }]

const area = [{
    'name' : 'Square millimeters (mm²)',
    'unit' : 45
} ,{ 
    'name' : 'Square centimeters (cm²)',
    'unit' : 45
} , {
    'name' : 'Square meters (m²)',
    'unit' : 45
} , {
    'name' : 'Square kilometers (km²)',
    'unit' : 45
} , {
    'name' : 'Hectare (ha)',
    'unit' : 45
} ,{ 
    'name' : 'Square inches (in²)',
    'unit' : 45
} , {
    'name' : 'Square feet (ft²)',
    'unit' : 45
} , {
    'name' : 'Square yards (yd²)',
    'unit' : 45
}]

const volume = [
    {'name' : 'Quart',
        'unit' : 34
    } , 
    {'name' : 'Fluid Ounce',
        'unit' : 34
    } , 
    {'name' : 'Teaspoon',
        'unit' : 34
    } , 
    {'name' : 'Liter',
        'unit' : 34
    } , 
    {'name' : 'Milliliter',
        'unit' : 34
    } , 
    {'name' : 'Tablespoon',
        'unit' : 34
    } , 
    {'name' : 'Gallon',
        'unit' : 34
    } , 
    {'name' : 'Pint',
        'unit' : 34
    } , 
    {'name' : 'Cup',
        'unit' : 34}
]

const weight = [
    {'name' : 'Milligram',
        'unit' : 75
    } ,
    {'name' : 'Grams',
        'unit' : 75
    },
    {'name' : 'Kilograms',
        'unit' : 75
    },
    {'name' : 'Pounds',
        'unit' : 75
    },
    {'name' : 'Tons',
        'unit' : 75
    } ,
    {'name' : 'Ounce',
        'unit' : 75
    }
]

const speed = []
const time = []
const angle = []
const pressure = []
const energy = []

let  convo_type = document.getElementById('type-conversion')
let type_from = document.getElementById('type-from')
let type_to = document.getElementById('type-to')


convo_type.addEventListener('change' ,function(){
    // console.log(convo_type)
    
    const conversionHTMLfrom = eval(convo_type.value).map((unit) => {
        return `<option id=${unit.name}>${unit.name}</option>`
    })
    
    const conversionHTMLto = eval(convo_type.value).map((unit) => {
        return `<option id="unit-to"  value=${unit.name}>${unit.name}</option>`
    })
    type_from.innerHTML = conversionHTMLfrom
    type_to.innerHTML = conversionHTMLto
    
})

let converBtn = document.getElementById('convert-btn')

converBtn.addEventListener('click' , function(){
    var x = document.getElementById("type-from")
    var i = x.selectedIndex;
    let dd_a_from_name = x.options[i].text
    
    let dropdown_unit_selected = eval(convo_type.value)
    
    
    
    
    var y = document.getElementById("type-to")
    var j = y.selectedIndex
    let dd_b_from_name = y.options[j].text
    
    let dd_a_from_unit = 0
    let dd_b_from_unit = 0
    
    let num = Number(document.getElementById('in-value').value)
    let unitResultHTML = document.getElementById('unit-result')
    
    console.log( `DD A : ${dd_a_from_name} ,  DD B :${dd_b_from_name}`)
    for( let k = 0 ; k < dropdown_unit_selected.length ; k++ ){
        if(dropdown_unit_selected[k].name === dd_a_from_name){
            dd_a_from_unit = dropdown_unit_selected[k].unit
        }
        if(dropdown_unit_selected[k].name === dd_b_from_name){
            dd_b_from_unit = dropdown_unit_selected[k].unit
        }
    }
    
    
    // console.log(dropdown_unit_selected[k])
    // console.log(dropdown_unit_selected[k].unit)
    // console.log( dropdown_unit_selected[k].unit)
    // console.log( y.options[j].text)
    // console.log( y.options[j].value)
    // console.log( x.options[i].text)
    // console.log( x.options[i].value)
    // console.log(convo_type.value)
    // console.log(convo_type.options.value)
    // console.log(eval(convo_type.value))
    // console.log(dropdown_unit_selected)
    // var k = convo_type.selectedIndex
    // console.log(k)
    // console.log(convo_type.value)
    // console.log(eval(convo_type.value))
    // console.log(evaSl(convo_type).options[1])
    
    let unitResult =  num * (dd_a_from_unit  *  dd_b_from_unit)





    console.log( num , dd_a_from_unit , dd_b_from_unit , unitResult )
   
    console.log(num * (dd_a_from_unit  *  dd_b_from_unit))
    console.log(unitResultHTML)
    
    unitResultHTML.innerText = unitResult
    // console.log('polin')
})