class PagesController < ApplicationController
  skip_before_action :authenticate_user!, only: [:home]

  def home
    if params[:word]
      @path = "app/assets/python/pal.py"
      @word = params[:word]
      @result = `python #{@path} #{@word}`
      @tekst = @word + @result
    else
      @word = "Enter word here"
      @tekst = "The answer will be here"
    end
  end
end
