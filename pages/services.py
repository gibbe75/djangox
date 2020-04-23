def PaginationService(objects_to_paginate, url_name, page = 1, elements_par_page=5, pagination_nb_displayed=5):

	paginator = Paginator(objects_to_paginate, elements_par_page)  # 5 notifs par page
	try:
		# La définition de nos URL autorise comme argument « page » uniquement 
		# des entiers, nous n'avons pas à nous soucier de PageNotAnInteger
		result = paginator.page(page)
	except EmptyPage:
		# Nous vérifions toutefois que nous ne dépassons pas la limite de page
		# Par convention, nous renvoyons la dernière page dans ce cas
		result = paginator.page(paginator.num_pages)


	current_page = result.number
	total_page_number = result.paginator.num_pages

	#si il n'y a qu'une page on renvoie rien
	if total_page_number <=1:
		return ({'result':result, 'pagination': '', 'pagination_mobile': ''})

	# on rend le nombre d'éléments à afficher impair
	if pagination_nb_displayed % 2 == 0:
		pagination_nb_displayed += 1

	pagination = []
	pagination.append({'current_page': False, 'label': 0})
	for page in result.paginator.page_range:
		temp = {}
		temp['current_page'] = False
		temp['label'] = page
		temp['page'] = page
		temp['link_to'] = reverse(url_name, kwargs={'page': page})
		
		# on affiche le numéro de la page quand :
			# page affichée
			# ou les pagination_nb_displayed-1 éléments autour de la page en cours
			# ou les pagination_nb_displayed premiers élements si on est dans les 1eres / dernieres pages
			# ou la page est un 

		if page == current_page \
		or (page > current_page - (pagination_nb_displayed + 1)/2 and page < current_page + (pagination_nb_displayed + 1)/2) \
		or (current_page - (pagination_nb_displayed - 1)/2 <=0 and page <= pagination_nb_displayed) \
		or (current_page + (pagination_nb_displayed - 1)/2 > total_page_number and page >= total_page_number - pagination_nb_displayed) \
		or ((current_page - page)%pagination_nb_displayed == 0 and abs((current_page - page)//pagination_nb_displayed) <= 2):
			if pagination[-1]['label'] != page-1:
				pagination.append({'current_page':False, 'label': "...", 'page': '', 'link_to': ''})
				temp['label'] = page
				temp['page'] = page
				temp['link_to'] = reverse(url_name, kwargs={'page': page}) 
			if page == current_page:
				temp['current_page'] = True	
			pagination.append(temp)

	pagination_f = pagination[1:]
	if result.has_previous():
		pagination_f.insert(0, {'current_page': False, 'label': 'Page précédente', 'link_to': reverse(url_name, kwargs={'page': current_page - 1})})
	if pagination_f[-1]['page']<total_page_number:
		pagination_f.append({'current_page': False, 'label': '...', 'link_to': ''})		
	if result.has_next():
		pagination_f.append({'current_page': False, 'label': 'Page suivante', 'link_to': reverse(url_name, kwargs={'page': current_page + 1})})

	# on construit également une pagination très petite pour écran mobile
	pagination_mobile = []
	pagination_mobile.append({'current_page': False, 'label': 0})
	for page in result.paginator.page_range:
		temp = {}
		temp['current_page'] = False
		temp['label'] = page
		temp['page'] = page
		temp['link_to'] = reverse(url_name, kwargs={'page': page})
		
		# on affiche le numéro de la page quand :
			# page affichée
			# ou les pagination_nb_displayed-1 éléments autour de la page en cours
			# ou les pagination_nb_displayed premiers élements si on est dans les 1eres / dernieres pages
			# ou la page est un 

		if page == current_page or page == current_page + 1 or page == current_page - 1:
			if pagination_mobile[-1]['label'] != page-1:
				pagination_mobile.append({'current_page':False, 'label': "...", 'page': '', 'link_to': ''})
				temp['label'] = page
				temp['page'] = page
				temp['link_to'] = reverse(url_name, kwargs={'page': page}) 
			if page == current_page:
				temp['current_page'] = True	
			pagination_mobile.append(temp)

	pagination_mobile_f = pagination_mobile[1:]
	
	if result.has_previous():
		pagination_mobile_f.insert(0, {'current_page': False, 'label': '<', 'link_to': reverse(url_name, kwargs={'page': current_page - 1})})
	if pagination_mobile_f[-1]['page']<total_page_number:
		pagination_mobile_f.append({'current_page': False, 'label': '...', 'link_to': ''})		
	if result.has_next():
		pagination_mobile_f.append({'current_page': False, 'label': '>', 'link_to': reverse(url_name, kwargs={'page': current_page + 1})})


	return ({'result':result, 'pagination': pagination_f, 'pagination_mobile': pagination_mobile_f})