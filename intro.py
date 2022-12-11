'''
Learning
	Supervised Learning: uses labeled inputs to train models and learn outputs
	Unsupervised Learning: uses patterns from inputs to learn outputs
	Reinforcement Learning: agent learning in an interactive environment based on rewards and penalties

Features
	Qualitative: finite number of categories of groups
		Nominal Data: categorical data without order, e.g. genders or countries
		Ordinal Data: categorical data with order, e.g. ages or moods

	Quantitative Data: numerically valued data (discrete or contiuous), e.g. height or cats owned

	One-hot Encoding: '1' if value matches category

Output
	Supervised
		Classification: predict discrete classes
			Multiclass: output the exact class, e.g. cat or dog or horse, plant species, types of fruit
			Binary: output Boolean, e.g. cat or NOT cat, positive or negative, spam or NOT spam
		
		Regression: predict continuous values, e.g. Apple stock, weather, the market

Model
	Training: create prediction vector from model, calculate loss between prediction and true values, make adjustments
	Validation: reality check during/after training to ensure model can handle unseen data
	Testing: checks how generalizable the final chosen model is 

	Loss: the closer the prediction is to the true value, the smaller the loss
		L1 Loss: loss = sum(|y_real - y_predicted|)
		L2 Loss: loss = sum((y_real - y_predicted) ** 2)
		Binary Cross-Entropy Loss: loss = -1/N * sum(y_real * log(y_predicted) + (1-y_real) * log((1-y_predicted)))
	
	Accuracy 
'''